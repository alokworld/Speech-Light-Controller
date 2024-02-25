// Define the LED pin
const int ledPin = 12;

void setup() {
  // Set the LED pin as an OUTPUT
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {

  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
  // Turn the LED on
   if (input == "lights on") {
  digitalWrite(ledPin, HIGH);
  delay(500); // Wait for 1 second

  // Turn the LED off
  digitalWrite(ledPin, LOW);
  delay(500); // Wait for 1 second
   }
  }}
