# Adapted from @CPlanner's example on Adafruit (3-1-19)
# This script may be used to test the MPU6050 module

# Import modules
import smbus
import math
from time import sleep

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

While True:

    Gyroscope_xout = read_word_2c(0x43)
    Gyroscope_yout = read_word_2c(0x45)
    Gyroscope_zout = read_word_2c(0x47)

    acceleration_xout = read_word_2c(0x3b)
    acceleration_yout = read_word_2c(0x3d)
    acceleration_zout = read_word_2c(0x3f)

    acceleration_xout_scaled = acceleration_xout / 16384.0
    acceleration_yout_scaled = acceleration_yout / 16384.0
    acceleration_zout_scaled = acceleration_zout / 16384.0

    print ("Gyro(scaled) in deg/sec - xout: ",acceleration_xout_scaled, " yout: ", acceleration_yout_scaled, " zout: ", acceleration_zout_scaled, " Accel(scaled) in gs - xout: ",acceleration_xout_scaled, " yout: ", acceleration_yout_scaled, " zout: ", acceleration_zout_scaled)
    sleep(1)