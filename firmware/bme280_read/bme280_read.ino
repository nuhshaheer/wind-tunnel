// bme280_read.ino
// Bench bring-up, walk-through step 1, item 6 (docs/electronics_walkthrough.md section 6): reads the Waveshare
// BME280 board and prints one line per second.
//
// Needs the "Adafruit BME280 Library" (Arduino IDE: Tools > Manage Libraries, search "Adafruit BME280",
// Install, and accept "Install all" for its dependencies). Record the version installed.
//
// Wiring (drawing sheet 12, DECISIONS.md D-018): VCC (red) -> 5V, GND (black) -> GND, SDA (blue) -> Mega 20,
// SCL (yellow) -> Mega 21; ADDR and CS left open, so the I2C address is 0x77.
//
// Output (Serial Monitor, 115200 baud), one line per second:
//   time_ms,p_Pa,T_C,RH_pct,sdp_factor
//   time_ms    : milliseconds since the board reset
//   p_Pa       : absolute (ambient) pressure, Pa
//   T_C        : temperature, degC (of the board, which warms itself slightly)
//   RH_pct     : relative humidity, %
//   sdp_factor : 96600 Pa / p_Pa, the factor every SDP810 reading gets multiplied by (Sensirion2024 notes:
//                dp_cor = dp_sensor x 966 mbar / p_amb). About 0.95 near sea level.
// Lines starting with '#' are messages, not data.

#include <Wire.h>
#include <Adafruit_BME280.h>

const uint8_t BME_ADDR = 0x77;
Adafruit_BME280 bme;

void setup() {
  Serial.begin(115200);
  Serial.println(F("# bme280_read: Waveshare BME280 at 0x77 (Adafruit BME280 Library, default settings)"));
  if (!bme.begin(BME_ADDR)) {
    Serial.println(F("# BME280 not found at 0x77 (or its chip ID is not 0x60). Check wiring; run i2c_scan."));
    while (true) {
      delay(1000);
    }
  }
  delay(100);  // let the first measurement finish
  Serial.println(F("time_ms,p_Pa,T_C,RH_pct,sdp_factor"));
}

// Reads the BME280's mode bits (register 0xF4 "ctrl_meas", bits 1:0). The library sets normal mode, 3.
// A chip that lost power or reset wakes in sleep mode, 0, and then only repeats its reset values
// (seen 2026-11-23: a frozen 71853.4 Pa, 23.90 degC, 80.2 %). Returns -1 if the chip did not answer.
int readMode() {
  Wire.beginTransmission(BME_ADDR);
  Wire.write(0xF4);
  if (Wire.endTransmission() != 0) {
    return -1;
  }
  if (Wire.requestFrom(BME_ADDR, (uint8_t)1) != 1) {
    return -1;
  }
  return Wire.read() & 0x03;
}

void loop() {
  int mode = readMode();
  if (mode != 3) {
    Serial.print(F("# BME280 not measuring (mode "));
    Serial.print(mode);
    Serial.println(F("): it lost power, reset or did not answer, likely a loose wire. Setting it up again."));
    if (!bme.begin(BME_ADDR)) {
      Serial.println(F("# BME280 not found at 0x77. Check its four wires."));
      delay(1000);
      return;
    }
    delay(100);  // let the first measurement finish
  }

  float p = bme.readPressure();     // Pa
  float t = bme.readTemperature();  // degC
  float rh = bme.readHumidity();    // %

  Serial.print(millis());
  Serial.print(',');
  Serial.print(p, 1);
  Serial.print(',');
  Serial.print(t, 2);
  Serial.print(',');
  Serial.print(rh, 1);
  Serial.print(',');
  Serial.println(96600.0 / p, 4);

  delay(1000);
}
