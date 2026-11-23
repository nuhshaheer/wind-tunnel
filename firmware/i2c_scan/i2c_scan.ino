// i2c_scan.ino
// Bench bring-up, walk-through section 6 (docs/electronics_walkthrough.md): lists every I2C address that
// answers on the Mega's SDA (pin 20) and SCL (pin 21), and reads the BME280's chip ID if it is there.
//
// Expected (drawing sheet 12, DECISIONS.md D-018):
//   0x77  Waveshare BME280 board (ADDR left open). Its chip ID (register 0xD0) should read 0x60;
//         0x58 would mean a BMP280 (no humidity), not a BME280.
//   0x25  Sensirion SDP810, once it is wired.
//
// Output: Serial Monitor at 115200 baud. The scan repeats every 5 s, so wires can be checked
// (with USB unplugged while changing them) and the result read again after reconnecting.
// Uses only the Wire library that comes with the Arduino IDE.

#include <Wire.h>

void setup() {
  Serial.begin(115200);
  Wire.begin();
  Wire.setClock(100000);            // 100 kHz, as on sheet 12
  Wire.setWireTimeout(25000, true); // give up after 25 ms instead of freezing if a wire is wrong
  Serial.println(F("# i2c_scan: scanning SDA pin 20 / SCL pin 21 every 5 s"));
}

void printHex(uint8_t value) {
  Serial.print(F("0x"));
  if (value < 16) {
    Serial.print('0');
  }
  Serial.print(value, HEX);
}

// Reads one byte from register 'reg' of the device at 'addr'. Sets ok to false on any I2C error.
uint8_t readRegister(uint8_t addr, uint8_t reg, bool &ok) {
  Wire.beginTransmission(addr);
  Wire.write(reg);
  if (Wire.endTransmission() != 0) {
    ok = false;
    return 0;
  }
  if (Wire.requestFrom(addr, (uint8_t)1) != 1) {
    ok = false;
    return 0;
  }
  ok = true;
  return Wire.read();
}

void loop() {
  uint8_t found = 0;
  Serial.println(F("Scanning..."));

  for (uint8_t addr = 1; addr < 127; addr++) {
    Wire.beginTransmission(addr);
    uint8_t err = Wire.endTransmission();

    if (Wire.getWireTimeoutFlag()) {
      Serial.println(F("  Bus timeout: SDA or SCL is stuck. Unplug USB and check those two wires."));
      Wire.clearWireTimeoutFlag();
      break;
    }
    if (err != 0) {
      continue; // nothing at this address
    }

    found++;
    Serial.print(F("  found "));
    printHex(addr);
    if (addr == 0x25) {
      Serial.print(F("  SDP810"));
    } else if (addr == 0x76 || addr == 0x77) {
      Serial.print(F("  BME280 board? chip ID "));
      bool ok;
      uint8_t id = readRegister(addr, 0xD0, ok);
      if (!ok) {
        Serial.print(F("could not be read"));
      } else {
        printHex(id);
        if (id == 0x60) {
          Serial.print(F(" = BME280, correct"));
        } else if (id == 0x58) {
          Serial.print(F(" = BMP280, not a BME280"));
        } else {
          Serial.print(F(" = unexpected"));
        }
      }
    }
    Serial.println();
  }

  if (found == 0) {
    Serial.println(F("  Nothing answered. Check: sensor power, SDA on pin 20, SCL on pin 21, pull-ups (the BME280 board has them)."));
  }
  Serial.println();
  delay(5000);
}
