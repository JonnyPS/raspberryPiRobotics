# CamJam EduKit 3 - Robotics
# Worksheet 5 - Line Detection

import RPi.GPIO as GPIO # import the GPIO Library
import time # Import the Time Library

# set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set variables for the GPIO pins
pinLineFollower = 25

# Set pin 25 as an inout so its value can be read
GPIO.setup(pinLineFollower, GPIO.IN)

try:
    # repeat the next indented block forever
    while True:
        # if the sensor is Low (=0), it's above the black line
        if GPIO.input(pinLineFollower)==0:
            print('The sensor is seeing a black surface BLACK BLACK BLACK')
        # if not (else), print the following
        else:
            print('The sensor is seeing a white surface WHITE WHITE WHITE')
        # wait, then do the same again
        time.sleep(0.2)

# if you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    GPIO.cleanup()

 
