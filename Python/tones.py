import RPi.GPIO as GPIO
import time

BuzzerPin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BuzzerPin, GPIO.OUT) 
GPIO.setwarnings(False)

global Buzz 
Buzz = GPIO.PWM(BuzzerPin, 440) 
Buzz.start(50)

# Three low buzzes to indicate a problem
for i in range(1, 3): 
	Buzz.ChangeFrequency(150) 
	time.sleep(1)
	Buzz.ChangeFrequency(1)
	time.sleep(.5)

time.sleep(2)

# One high buzz to indicate all clear
Buzz.ChangeFrequency(2000)
time.sleep(3)
Buzz.ChangeFrequency(1)

GPIO.cleanup()
