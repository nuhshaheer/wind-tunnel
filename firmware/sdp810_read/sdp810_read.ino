// sdp810_read.ino
// Bench bring-up, walk-through step 2 (docs/electronics_walkthrough.md section 6): reads the Sensirion
// SDP810-125Pa differential pressure sensor and prints one averaged line per second.
//
// Wiring (drawing sheet 12, DECISIONS.md D-018): SDP810 pin 1 SCL -> Mega 21, pin 2 VDD -> 5V, pin 3 GND -> GND,
// pin 4 SDA -> Mega 20. I2C address 0x25. The BME280 board on the same bus supplies the pull-ups.
//
// Output (Serial Monitor, 115200 baud), one line per second:
//   time_ms,dp_Pa,sensor_T_C,bad_reads
//   time_ms    : milliseconds since the board reset
//   dp_Pa      : differential pressure High port minus Low port, in Pa, the mean of READS_PER_LINE reads.
//                As read: the ambient-pressure correction (x 966 mbar / p_amb, Sensirion2024 notes) is NOT applied.
//   sensor_T_C : the sensor chip's own temperature, degC (not the air temperature; datasheet footnote 4)
//   bad_reads  : reads in this line that failed (no data yet, or a checksum error); should be 0
// Lines starting with '#' are messages, not data.
//
// Sensor facts used (SDP8xx datasheet v1.1, resources/notes/SDP8xx.md; pages 7 and 10 rechecked 2026-11-23):
//   start continuous measurement, differential-pressure compensation, average till read: command 0x3615
//   stop continuous measurement: 0x3FF9 (sensor accepts a new command 500 us later)
//   first result 8 ms after the start; small deviations for the next 12 ms
//   each read: 9 bytes = DP msb, lsb, CRC, Temp msb, lsb, CRC, DP scale factor msb, lsb, CRC
//   dp in Pa = signed reading / scale factor (240 per Pa for the 125 Pa part); T in degC = reading / 200
//   CRC-8: polynomial 0x31, initial 0xFF, no reflection, no final XOR; CRC(0xBEEF) = 0x92

#include <Wire.h>

const uint8_t SDP_ADDR = 0x25;
const uint8_t READS_PER_LINE = 10;
const unsigned long READ_INTERVAL_MS = 100;

uint8_t crc8(uint8_t msb, uint8_t lsb) {
  uint8_t crc = 0xFF;
  uint8_t data[2] = {msb, lsb};
  for (uint8_t i = 0; i < 2; i++) {
    crc ^= data[i];
    for (uint8_t bit = 0; bit < 8; bit++) {
      if (crc & 0x80) {
        crc = (uint8_t)((crc << 1) ^ 0x31);
      } else {
        crc = (uint8_t)(crc << 1);
      }
    }
  }
  return crc;
}

bool sendCommand(uint16_t command) {
  Wire.beginTransmission(SDP_ADDR);
  Wire.write((uint8_t)(command >> 8));
  Wire.write((uint8_t)(command & 0xFF));
  return Wire.endTransmission() == 0;
}

int16_t toSigned(uint8_t msb, uint8_t lsb) {
  return (int16_t)(((uint16_t)msb << 8) | lsb);
}

// Reads one result. Returns false if the sensor has no data yet (it NACKs) or a checksum fails.
bool readSDP(int16_t &dpRaw, int16_t &tempRaw, int16_t &scale) {
  uint8_t received = Wire.requestFrom(SDP_ADDR, (uint8_t)9);
  if (received != 9) {
    while (Wire.available()) {
      Wire.read();
    }
    return false;
  }
  uint8_t b[9];
  for (uint8_t i = 0; i < 9; i++) {
    b[i] = Wire.read();
  }
  for (uint8_t w = 0; w < 3; w++) {  // three 16-bit words, each followed by its CRC
    if (crc8(b[3 * w], b[3 * w + 1]) != b[3 * w + 2]) {
      return false;
    }
  }
  dpRaw = toSigned(b[0], b[1]);
  tempRaw = toSigned(b[3], b[4]);
  scale = toSigned(b[6], b[7]);
  return true;
}

void setup() {
  Serial.begin(115200);
  Wire.begin();
  Wire.setClock(100000);            // 100 kHz, as on sheet 12
  Wire.setWireTimeout(25000, true); // give up instead of freezing if a wire is wrong

  Serial.println(F("# sdp810_read: SDP810-125Pa at 0x25, continuous mode 0x3615 (average till read)"));
  if (crc8(0xBE, 0xEF) != 0x92) {
    Serial.println(F("# CRC self-test FAILED: program error, readings cannot be trusted"));
  }

  // The sensor keeps its power when the Mega resets after an upload, so it may still be measuring.
  // Stop it first; an error here is harmless.
  sendCommand(0x3FF9);
  delay(2);
  if (!sendCommand(0x3615)) {
    Serial.println(F("# The SDP810 did not accept the start command. Check its wiring, then unplug and replug USB."));
  }
  delay(20);  // first result after 8 ms, small deviations for the next 12 ms

  // Report the scale factor once, so it can be checked against the datasheet (240 for the 125 Pa part).
  int16_t dpRaw, tempRaw, scale;
  if (readSDP(dpRaw, tempRaw, scale)) {
    Serial.print(F("# scale factor read from the sensor: "));
    Serial.print(scale);
    Serial.println(F(" counts per Pa (expected 240)"));
  } else {
    Serial.println(F("# first read failed; continuing"));
  }
  Serial.println(F("time_ms,dp_Pa,sensor_T_C,bad_reads"));
}

void loop() {
  long sumDp = 0;
  long sumTemp = 0;
  int16_t scale = 0;
  uint8_t good = 0;
  uint8_t bad = 0;

  for (uint8_t i = 0; i < READS_PER_LINE; i++) {
    delay(READ_INTERVAL_MS);
    int16_t dpRaw, tempRaw, sc;
    if (readSDP(dpRaw, tempRaw, sc)) {
      sumDp += dpRaw;
      sumTemp += tempRaw;
      scale = sc;
      good++;
    } else {
      bad++;
    }
  }

  if (good == 0 || scale <= 0) {
    Serial.println(F("# No valid reading in the last second. Check the SDP810 wiring; unplug and replug USB."));
    return;
  }

  float dpPa = (float)sumDp / good / scale;
  float tempC = (float)sumTemp / good / 200.0;

  Serial.print(millis());
  Serial.print(',');
  Serial.print(dpPa, 3);
  Serial.print(',');
  Serial.print(tempC, 2);
  Serial.print(',');
  Serial.println(bad);
}
