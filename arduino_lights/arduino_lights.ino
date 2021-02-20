int redPin = 11;                // output pin number to Red pin of the LED
int greenPin = 10;              // output pin number to Green pin
int bluePin = 9;                // output pin number to Blue pin

void setup()                    // this runs once, when the sketch starts
{
 pinMode(redPin, OUTPUT);      // sets the pin as output pin
 pinMode(greenPin, OUTPUT);    // sets the pin as output pin
 pinMode(bluePin, OUTPUT);     // sets the pin as output pin
}

void loop()                     // this runs over and over again forever
{
 int sentiment = -1;
 int threshold = .2;
 
 delay(1000);

 if (sentiment <= -.2) {
  analogWrite(redPin, 255);
  analogWrite(bluePin, 0);
  analogWrite(greenPin, 0);
 }

 else if (sentiment <= .2) {
  analogWrite(greenPin, 0);
  analogWrite(bluePin, 255);
  analogWrite(redPin, 0);
 }

 else if (sentiment > .2) {
  analogWrite(redPin, 0);
  analogWrite(bluePin, 0);
  analogWrite(greenPin, 255);
 }
 
}
