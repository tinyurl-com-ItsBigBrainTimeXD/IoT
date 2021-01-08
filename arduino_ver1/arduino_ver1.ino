#include <SoftwareSerial.h>
#include "Ultrasonic.h"
Ultrasonic ultrasonic(4); // include Seeed Studio ultrasonic ranger library

#include <Wire.h>        // include Arduino Wire library

#include <Servo.h>

const int buzzer = 7;

// defines variables
long duration;
int distance;

int pbPin = 12;   // choose the input pin (for a pushbutton)
int val = 0;     // variable for reading the pin status

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

void setup() {
   
  pinMode(pbPin, INPUT);    // declare pushbutton as input

  pinMode(buzzer, OUTPUT);
  
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object

  Serial.begin(9600);
}

void loop() {

//  seeed_ultrasonic();

//  buzzer_sound();


  lid_close();
  
  Serial.println("Lid closed, waiting for PB");
  button_read();
  
  lid_open();
  Serial.println("Lid open, waiting for PB");
  
  button_read();

  
}

void button_read(){
  val = digitalRead(pbPin);  // read input value
  while (val == LOW) {
    val = digitalRead(pbPin);  // read input value
  }
}


void lid_close() {
  for (pos = 0; pos <= 90; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}

void lid_open() {
  for (pos = 90; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
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


void seeed_ultrasonic() {
    long RangeInCentimeters;
    RangeInCentimeters = ultrasonic.read();
    delay(150);
    Serial.print("Distance: ");
    Serial.print(RangeInCentimeters,DEC);
    Serial.print(" cm");
    Serial.println("");
}
