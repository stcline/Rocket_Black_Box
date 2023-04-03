# Attach a button to GPIO 23 and set it up as an input
# When the button is pressed, another script is run
# The script is run as a background process so the button can be pressed again

import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(23)
    if input_state == False:
        print('Button Pressed')
        subprocess.Popen(['python', 'RBB.py'])
        time.sleep(0.2)

