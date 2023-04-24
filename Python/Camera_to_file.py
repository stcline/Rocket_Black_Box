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

def camera_rec():
	filename = '/home/pi/Documents/Rocket_Black_Box/Python/videos/rocket_vid' + datetime.datetime.now().strftime("%Y%m%d-%H%M%S" + str(rectime))
	camera.start_preview()
	camera.start_recording(filename + '.h264')
	sleep(rectime)
	camera.stop_recording()
	camera.stop_preview()

camera_rec()
GPIO.cleanup()