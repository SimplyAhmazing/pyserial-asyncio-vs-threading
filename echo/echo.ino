void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    Serial.println(Serial.read());
    digitalWrite(13, HIGH);
    delay(100); 
  }
  digitalWrite(13, LOW); 
}
