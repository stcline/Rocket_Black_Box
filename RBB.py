#!/usr/bin/env python3
"""
This script runs a Raspberry Pi Zero W in order to record flight data.

The equipment included in this device are:
  - Raspberry Pi Zero W
  - HD Camera Module with wide angle lens
  - GY-521 3 Axis Accelerometer Gyroscope Module
  - piezoelelctric buzzer
  - LED of any color

The script does the following:
  - waits for button to be pressed to arm
  - waits for a second press to begin
  - when pressed, begins a timer
  - plays a tone indicating it is ready
  - turns on an indicator light when recording begins
  - begins recording video
  - begins recording accelleration and 6 DOF axis position (maybe GPS too)
"""

# import modules

# Run other scripts using the method:
#   with open ("other.py) as f:
#     exec(f.read())
#  https://www.w3docs.com/snippets/python/how-can-i-make-one-python-file-run-another.html#:~:text=To%20run%20one%20Python%20file,function%20or%20the%20subprocess%20module.&text=This%20will%20execute%20the%20code,in%20the%20main.py%20file.&text=This%20will%20run%20the%20other.py%20script%20as%20a%20separate%20process.

