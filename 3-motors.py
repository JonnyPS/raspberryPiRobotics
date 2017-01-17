#CamJam EduKit 3 - Robotics
#Worksheet 3 - Motor Test Code

import RPi.GPIO as GPIO  # Import the GPIO library
import time # import the time library

#set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set the GPIO pin mode
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

# turn all motors off
GPIO.output(7, 0)
GPIO.output(8, 0)
GPIO.output(9, 0)
GPIO.output(10, 0)

# turn the right motor forwards
GPIO.output(9, 1)
GPIO.output(10, 0)

# turn the left motor forwards
GPIO.output(7, 0)
GPIO.output(8, 1)

#Wait for 1 second
time.sleep(0.5)
# reset the GPIO pins (turns off motors too)
GPIO.cleanup()


