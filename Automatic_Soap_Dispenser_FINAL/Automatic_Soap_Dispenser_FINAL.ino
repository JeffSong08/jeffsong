#include <LiquidCrystal.h>

#include <Wire.h>


LiquidCrystal_I2C lcd(0x27, 20, 4);

#include <Servo.h>

Servo myservo;

const int trigPin = 8;
const int echoPin = 7;

int ledpin = 10;

long duration;
int distance;

int Redpin = 3;
int Greenpin = 4;
int Bluepin = 5;

int colour = 0;

void setup() {
  myservo.attach(9);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode( Redpin , OUTPUT);
  pinMode( Greenpin , OUTPUT);
  pinMode( Bluepin , OUTPUT);
  pinMode( ledpin , OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;
  Serial.print("Distance: ");
  Serial.println(distance);


  if (distance < 7)
  {
    delay(3000);
    myservo.write(0);
    delay(1);
    myservo.write(360);
    delay(1000);
    digitalWrite(ledpin, LOW);

    lcd.init();
    lcd.init();

    analogWrite( Redpin , 100 );
    analogWrite( Greenpin , 0);
    analogWrite( Bluepin , 0 );

    lcd.backlight();
    
    lcd.setCursor(1, 0);
    lcd.print("Wash your Hands");
    lcd.setCursor(1, 1);
    lcd.print("  20 seconds");
    lcd.setCursor(1, 1);
    lcd.print("  20 seconds");
    delay(2000);
    lcd.clear();

    lcd.setCursor(1, 0);
    lcd.print("Time Remaining");
    lcd.setCursor(1, 1);
    lcd.print("      20");
    delay(1000);
    lcd.setCursor(1, 1);
    lcd.print("      19");
    delay(1000);
    lcd.setCursor(1, 1);
    lcd.print("      18");
    delay(1000);
    lcd.setCursor(1, 1);
    lcd.print("      17");
    delay(1000);
    lcd.setCursor(1, 1);
    lcd.print("      16");
    delay(1000);
    lcd.setCursor(1, 1);
    lcd.print("      15");
    delay(1000);
    lcd.setCursor(1, 1);
    lcd.print("      14");
    delay(1000);
    lcd.setCursor(1, 1);
    lcd.print("      13");
    delay(1000);
    lcd.setCursor(1, 1);
    lcd.print("      12");
    delay(1000);
    lcd.setCursor(1, 1);
    lcd.print("      11");
    delay(1000);
    lcd.setCursor(1, 1);
    lcd.print("      10");
    delay(1000);
    lcd.setCursor(1, 1);
    lcd.print("      2");
    lcd.clear();
    delay(10);
    lcd.setCursor(1, 0);
    lcd.print("Time Remaining");
    lcd.setCursor(1, 1);
    lcd.print("      09");
    delay(1000);
    lcd.setCursor(1, 1);
    lcd.print("      08");
    delay(1000);
    lcd.setCursor(1, 1);
    lcd.print("      07");
    delay(1000);
    lcd.setCursor(1, 1);
    lcd.print("      06");
    delay(1000);
    lcd.setCursor(1, 1);
    lcd.print("      05");
    delay(1000);
    lcd.setCursor(1, 1);
    lcd.print("      04");
    delay(1000);
    lcd.setCursor(1, 1);
    lcd.print("      03");
    delay(1000);
    lcd.setCursor(1, 1);
    lcd.print("      02");
    delay(1000);
    lcd.setCursor(1, 1);
    lcd.print("      01");
    delay(1000);
    lcd.print("      01");
    delay(10);
    lcd.clear();
    lcd.setCursor(1, 0);
    lcd.print(" It's time to");
    lcd.setCursor(1, 1);
    lcd.print(" rinse hands!");
    analogWrite( Redpin , 0);
    analogWrite( Greenpin , 0);
    analogWrite( Bluepin , 100);
    delay(10000);
    lcd.clear();
    digitalWrite(ledpin, HIGH);
    lcd.setCursor(1, 0);
    lcd.setCursor(1, 0);
    lcd.print("     Let's");
    lcd.setCursor(1, 1);
    lcd.print("  Wash Hands");
  }
  else
  {
    myservo.write(0);

    analogWrite( Redpin , 0);
    analogWrite( Greenpin , 0);
    analogWrite( Bluepin , 0);


  }

}
