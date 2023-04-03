# Steve Cline - April 3, 2023
"""This script runs a Raspberry Pi Zero W in order to record flight data.

The equipment included in this device are:
  - Raspberry Pi Zero W
  - HD Camera Module with wide angle lens
  - MPU6050 Accelerometer Gyroscope Module
  - button module and a 1.6k ohm resistor (GPIO 23)
  - piezoelelctric buzzer (GPIO 4)
  - LED of any color (GPIO 17)

The script does the following:
  - flashes an LED and buzzes a buzzer 10 times to indicate it is running
  - waits for a button to be pressed
  - turns on an indicator light when recording begins
  - begins recording video
  - begins recording accelleration and 6 DOF axis position (maybe GPS too)
  - runs for 5 minutes
"""

import RPi.GPIO as GPIO
import time
import subprocess

buttonPin = 23
BuzzerPin = 4
ledPin = 17

# Set up the button
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set up the buzzer
GPIO.setup(BuzzerPin, GPIO.OUT)
GPIO.setwarnings(False)
Buzz = GPIO.PWM(BuzzerPin, 440)

# Flash LED and buzz 10 times to indicate that the script is running
for i in range(10):
    GPIO.output(ledPin, GPIO.HIGH)
    Buzz.start(50)
    time.sleep(0.1)
    GPIO.output(ledPin, GPIO.LOW)
    Buzz.stop()
    time.sleep(0.1)

while True:
    input_state = GPIO.input(buttonPin)
    if input_state == False:
        print('Button Pressed')
        GPIO.output(ledPin, GPIO.HIGH)
        subprocess.Popen(['python3', 'black_box_led.py'])
        subprocess.Popen(['python3', 'MPU6050_CSV.py'])
        time.sleep(0.2)