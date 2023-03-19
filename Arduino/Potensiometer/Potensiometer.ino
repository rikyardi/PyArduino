int potPin = A0;
int potVal;

void setup() {
  Serial.begin(115200);
  pinMode(potPin, INPUT);
}

void loop() {
  potVal = analogRead(potPin);
  Serial.println(potVal);
  delay(1000);

}
