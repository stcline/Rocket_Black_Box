'''
  Read Gyro and Accelerometer by Interfacing Raspberry Pi with MPU6050 using Python
	http://www.electronicwings.com
  
  This modification to the script will print output to a csv 20 times per second.
'''
import smbus			#import SMBus module of I2C
import math
import time
import datetime
import csv

# Register setup
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

# Read register data
def read_byte(reg):
	return bus.read_byte_data(address, reg)

def read_word(reg):
	h = bus.read_byte_data(address, reg)
	l = bus.read_byte_data(address, reg +1)
	value = (h << 8) + l
	return value

def read_word_2c(reg):
	val = read_word(reg)
	if (val >= 0x8000):
		return -((65535 - val) + 1)
	else:
		return val

# Convert raw register data to x,y and accelleration
def dist(a ,b):
	return math.sqrt(( a *a ) +( b *b))

def get_y_rotation(x ,y ,z):
	radians = math.atan2(x, dist(y ,z))
	return -math.degrees(radians)

def get_x_rotation(x ,y ,z):
	radians = math.atan2(y, dist(x ,z))
	return math.degrees(radians)

bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
address = 0x68       # via i2cdetect

# Activate module
bus.write_byte_data(address, power_mgmt_1, 0)

print (" Reading Data of Gyroscope and Accelerometer")

# timeout = time.time() + 60*5   # 5 minutes from now
timeout = time.time() + 5   # 5 seconds from now

while True:
	Gx = read_word_2c(0x43)
	Gy = read_word_2c(0x45)
	Gz = read_word_2c(0x47)

	Ax = read_word_2c(0x3b)
	Ay = read_word_2c(0x3d)
	Az = read_word_2c(0x3f)

	Ax_scaled = Ax / 16384.0
	Ay_scaled = Ay / 16384.0
	Az_scaled = Az / 16384.0

	print ("Gx=%.2f" %Gx, u'\u00b0'+ "/s", "\tGy=%.2f" %Gy, u'\u00b0'+ "/s", "\tGz=%.2f" %Gz, u'\u00b0'+ "/s", "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az)
  
	now = datetime.datetime.now()
	with open('/home/pi/Documents/Rocket_Black_Box/Logs/rocketlog.csv', 'a', newline='') as csvfile:
		logwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		logwriter.writerow([now.strftime("%Y")] + [now.strftime("%d")] + [now.strftime("%m")] + [now.strftime("%H")] + [now.strftime("%M")] + [now.strftime("%S.%f")] + [Gx] + [Gy] + [Gz] + [Ax] +[Ay] + [Az] + [Ax_scaled] + [Ay_scaled] + [Az_scaled])
  
	time.sleep(.01)

	if time.time() > timeout:
		break