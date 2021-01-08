#include <SoftwareSerial.h>
#include "Ultrasonic.h"
Ultrasonic ultrasonic(4); // include Seeed Studio ultrasonic ranger library

#include <Wire.h>        // include Arduino Wire library

#include <Servo.h>
const int buzzer = 7;
// defines variables
long duration;
int distance;

int ledPin = 13;                // LED 
int pirPin = 2;                 // PIR Out pin 
int pirStat = 0;  

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

void setup() {
  pinMode(ledPin, OUTPUT);     
  pinMode(pirPin, INPUT); 

  pinMode(buzzer, OUTPUT);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object

  Serial.begin(9600);
}

void loop() {

  seeed_ultrasonic();

  motion_sensor();

//  buzzer_sound();

//  servo1();
}

void servo1() {
  for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}

void buzzer_sound() {
  tone(buzzer, 1000); // Send 1KHz sound signal...
  delay(1000); 
  noTone(buzzer);     // Stop sound...
  delay(1000); 
}


void motion_sensor() {
   pirStat = digitalRead(pirPin); 
   
  if (pirStat == HIGH) {            // if motion detected
    digitalWrite(ledPin, HIGH);  // turn LED ON
  } 
  else {
    digitalWrite(ledPin, LOW); // turn LED OFF if we have no motion  
  }
}


void seeed_ultrasonic() {
    long RangeInCentimeters;
    RangeInCentimeters = ultrasonic.read();
    delay(150);
    Serial.print("Distance: ");
    Serial.print(RangeInCentimeters,DEC);
    Serial.print(" cm");
    Serial.println("");
    
}
