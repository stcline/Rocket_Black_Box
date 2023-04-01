# Adapted from @CPlanner's example on Adafruit (3-1-19) 
# This script may be used to test the MPU6050 module
# Read data from MPU6050

# Import modules
import smbus
import math

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

# Print raw and converted data from module
print ("Gyroscope")
print ("---------")

Gyroscope_xout = read_word_2c(0x43)
Gyroscope_yout = read_word_2c(0x45)
Gyroscope_zout = read_word_2c(0x47)

print ("Gyroscope_xout: ", ("%5d" % Gyroscope_xout), " scaled: ", (Gyroscope_xout / 131))
print ("Gyroscope_yout: ", ("%5d" % Gyroscope_yout), " scaled: ", (Gyroscope_yout / 131))
print ("Gyroscope_zout: ", ("%5d" % Gyroscope_zout), " scaled: ", (Gyroscope_zout / 131))

print ()
print ("Accelerometer")
print ("-------------")

acceleration_xout = read_word_2c(0x3b)
acceleration_yout = read_word_2c(0x3d)
acceleration_zout = read_word_2c(0x3f)

acceleration_xout_skaliert = acceleration_xout / 16384.0
acceleration_yout_skaliert = acceleration_yout / 16384.0
acceleration_zout_skaliert = acceleration_zout / 16384.0

print ("acceleration_xout: ", ("%6d" % acceleration_xout), " scaled: ", acceleration_xout_skaliert)
print ("acceleration_yout: ", ("%6d" % acceleration_yout), " scaled: ", acceleration_yout_skaliert)
print ("acceleration_zout: ", ("%6d" % acceleration_zout), " scaled: ", acceleration_zout_skaliert)

print ("X Rotation: " , get_x_rotation(acceleration_xout_skaliert, acceleration_yout_skaliert, acceleration_zout_skaliert))
print ("Y Rotation: " , get_y_rotation(acceleration_xout_skaliert, acceleration_yout_skaliert, acceleration_zout_skaliert))
