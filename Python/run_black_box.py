# Attach a button to GPIO 23 and set it up as an input
# Attach a buzzer to GPIO 4 and set it up as an output
# Attach an LED to GPIO 17 and set it up as an output
# An LED will flash and a buzzer will sound ten times to indicate that the script is running
# When the button is pressed, all the scripts are run

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
        subprocess.Popen(['python', 'black_box_led.py'])
        subprocess.Popen(['python', 'MPU6050_CSV.py'])
        time.sleep(0.2)