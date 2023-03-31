int potPin = A0;
int readVal;
float potVal;

void setup() {
  Serial.begin(115200);

}

void loop() {
  readVal = analogRead(potPin);
  potVal = (5./1023.)*readVal;
  Serial.println(potVal);
  delay(500);
}
