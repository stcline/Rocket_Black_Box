# Rocket Black Box
### This project runs a "black box" operation for a model rocket.  The scripts are meant to run on a Raspberry Pi Zero W to record an HD video as well as acceleration and direction data during the flight.

### Equipment
- [Raspberry Pi Zero W](https://www.amazon.com/Raspberry-Pi-Zero-Wireless-model/dp/B06XFZC3BX)
- Micro SD Card (16GB)
- External battery pack (The Pi Zero runs at 3.3V)
- [Pi Camera Module (This particular project uses a wide angle lens)](https://www.amazon.com/dp/B09D8LSN5M?ref=ppx_yo2ov_dt_b_product_details&th=1)
- [MPU6050 Accelerometer/Gyroscope](https://www.amazon.com/HiLetgo-MPU-6050-Accelerometer-Gyroscope-Converter/dp/B078SS8NQV)

### Hardware Setup

### Code
There are two scripts running simultaneously after the Pi reboots.  The first script controls the camera

AdaFruit CircuitPython with the BME 280:
https://github.com/adafruit/Adafruit_CircuitPython_BME280

MPU6050 Gyroscope: https://www.electronicwings.com/sensors-modules/mpu6050-gyroscope-accelerometer-temperature-sensor-module
With RPi: https://www.electronicwings.com/raspberry-pi/mpu6050-accelerometergyroscope-interfacing-with-raspberry-pi

Video Naming Convention:


![Rocket_vid_name](https://user-images.githubusercontent.com/22602103/224872636-065e27c9-b785-46be-bd47-c3e3e41daad3.png)
