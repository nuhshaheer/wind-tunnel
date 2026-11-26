// hx711_raw_counts.ino
// Bench bring-up, walk-through step 3 (docs/electronics_walkthrough.md section 6):
// reads raw counts from the SparkFun HX711 board and prints each reading over USB.
//
// Wiring (drawing sheet 12, DECISIONS.md D-018):
//   HX711 DAT -> Mega pin 2      HX711 CLK -> Mega pin 3
//   HX711 VCC and VDD -> 5V      HX711 GND -> GND
//   Load cell: red -> RED, black -> BLK, white -> WHT, green -> GRN (YLW empty)
//
// Output (Serial Monitor, 115200 baud), one line per reading:
//   time_ms,counts
//   time_ms : milliseconds since the board reset
//   counts  : raw HX711 reading, channel A, gain 128. A signed whole number from -8388608 to 8388607,
//             in ADC counts. No calibration is applied: grams come later, from the calibration run.
// Lines starting with '#' are messages, not data.
//
// The gap between time_ms values shows the HX711's sample rate, set by its RATE jumper:
//   about 100 ms apart = 10 samples/s, about 12.5 ms apart = 80 samples/s.
//
// AVERAGE_OVER sets how many readings go into each printed line (their mean, cut to a whole count toward zero):
//   1  = every raw reading (about 10 lines a second at the RATE found on 2026-11-23);
//   10 = one line a second, short enough to copy a whole penny test from the Serial Monitor.
// The gap rule above then applies per reading, not per line.
//
// For the Serial Plotter, set FOR_PLOTTER to true and upload again: it then prints only the counts.
//
// No library needed. Protocol from the HX711 datasheet (resources/notes/HX711.md): DAT goes LOW when a
// reading is ready; 24 clock pulses shift it out, most significant bit first; a 25th pulse selects
// channel A, gain 128 for the next reading. CLK held HIGH for more than 60 us powers the chip down,
// so the pulses are kept short.

const uint8_t PIN_DAT = 2;
const uint8_t PIN_CLK = 3;
const bool FOR_PLOTTER = false;
const uint8_t AVERAGE_OVER = 1;

void setup() {
  Serial.begin(115200);
  pinMode(PIN_DAT, INPUT);
  pinMode(PIN_CLK, OUTPUT);
  digitalWrite(PIN_CLK, LOW);  // LOW = HX711 awake

  if (FOR_PLOTTER) {
    Serial.println(F("counts"));
  } else {
    Serial.println(F("# hx711_raw_counts: channel A, gain 128. Ignore the first second (settling)."));
    Serial.print(F("# each line: mean of "));
    Serial.print(AVERAGE_OVER);
    Serial.println(F(" reading(s)"));
    Serial.println(F("time_ms,counts"));
  }
}

long readHX711() {
  unsigned long value = 0;

  noInterrupts();  // keep every CLK HIGH pulse far below 60 us
  for (uint8_t i = 0; i < 24; i++) {
    digitalWrite(PIN_CLK, HIGH);
    delayMicroseconds(1);
    value = (value << 1) | (digitalRead(PIN_DAT) == HIGH ? 1UL : 0UL);
    digitalWrite(PIN_CLK, LOW);
    delayMicroseconds(1);
  }
  // 25th pulse: next reading on channel A, gain 128
  digitalWrite(PIN_CLK, HIGH);
  delayMicroseconds(1);
  digitalWrite(PIN_CLK, LOW);
  interrupts();

  // The 24-bit reading is two's complement: copy the sign bit into the top 8 bits.
  if (value & 0x800000UL) {
    value |= 0xFF000000UL;
  }
  return (long)value;
}

// Waits for DAT to go LOW (reading ready), complaining once a second if it never does, then reads.
long waitAndRead() {
  unsigned long waitStart = millis();
  while (digitalRead(PIN_DAT) == HIGH) {
    if (millis() - waitStart > 1000) {
      Serial.println(F("# No reading from the HX711 for 1 s: check VCC, VDD, GND, DAT on pin 2, CLK on pin 3."));
      waitStart = millis();
    }
  }
  return readHX711();
}

void loop() {
  long sum = 0;  // at most 255 x 8388608, well inside a long
  for (uint8_t i = 0; i < AVERAGE_OVER; i++) {
    sum += waitAndRead();
  }
  long counts = sum / AVERAGE_OVER;

  if (FOR_PLOTTER) {
    Serial.println(counts);
  } else {
    Serial.print(millis());
    Serial.print(',');
    Serial.println(counts);
  }
}
