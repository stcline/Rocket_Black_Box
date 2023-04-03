#!/usr/bin/env python3
"""
This script runs a Raspberry Pi Zero W in order to record flight data.

The equipment included in this device are:
  - Raspberry Pi Zero W
  - HD Camera Module with wide angle lens
  - MPU6050 Accelerometer Gyroscope Module
  - piezoelelctric buzzer
  - LED of any color

The script does the following:
  - flashes an LED and buzzes a buzzer 10 times to indicate it is running
  - waits for a button to be pressed
  - turns on an indicator light when recording begins
  - begins recording video
  - begins recording accelleration and 6 DOF axis position (maybe GPS too)
  - runs for 5 minutes
"""

# import libraries

# Run other scripts using the method:
with open ("black_box_led.py") as f:
  exec(f.read())
#  https://www.w3docs.com/snippets/python/how-can-i-make-one-python-file-run-another.html#:~:text=To%20run%20one%20Python%20file,function%20or%20the%20subprocess%20module.&text=This%20will%20execute%20the%20code,in%20the%20main.py%20file.&text=This%20will%20run%20the%20other.py%20script%20as%20a%20separate%20process.

