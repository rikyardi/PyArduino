int x = 1;
int y = 3;
int z = 5;

void setup() {
  Serial.begin(115200);
}

void loop() {
  x=x+2;
  y=y+4;
  z=z+6;
  
  Serial.print(x);
  Serial.print(",");
  Serial.print(y);
  Serial.print(",");
  Serial.println(z); 
  delay(1000);
}
