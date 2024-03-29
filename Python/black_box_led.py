'''
Script turns camera on and records for five minutes.  Saves to dated file.

'''
from picamera import PiCamera
from time import sleep
import time
import datetime
import RPi.GPIO as GPIO

#Set up the camera
camera = PiCamera()
rectime = 5 #recording time (5 seconds is for testing only - change to 300 at final)
camera.rotation = 180

#Set up the indicator light
GPIO.setmode(GPIO.BOARD)
led = 12 # GPIO pin number is 5 and name is GPIO3
GPIO.setup(led, GPIO.OUT, initial = 0) # Setup LED and set it initially to OFF

def camera_rec():
	filename = '/home/pi/Documents/Rocket_Black_Box/Python/videos/rocket_vid' + datetime.datetime.now().strftime("%Y%m%d-%H%M%S" + str(rectime))
	camera.start_preview()
	camera.start_recording(filename + '.h264')
	sleep(rectime)
	camera.stop_recording()
	camera.stop_preview()


GPIO.output(led, GPIO.HIGH)
camera_rec()
GPIO.output(led, GPIO.LOW)
GPIO.cleanup()
