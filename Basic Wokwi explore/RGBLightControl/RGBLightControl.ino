int redPin = 11;
int greenPin = 10;
int bluePin = 9;
int dly = 400;

void setup(){
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop(){
  digitalWrite(redPin, HIGH);
  delay(dly);
  digitalWrite(redPin, LOW);
  delay(dly);
  digitalWrite(greenPin, HIGH);
  delay(dly);
  digitalWrite(greenPin, LOW);
  delay(dly);
  digitalWrite(bluePin, HIGH);
  delay(dly);
  digitalWrite(bluePin, LOW);
  delay(dly);
}