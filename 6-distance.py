# CamjAM EduKit 3 - Robotics
# Worksheet 6 - Measuring Distance

import RPi.GPIO as GPIO # import the GPIO library
import time # import the time library

# set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO pins to use on the PI
pinTrigger = 17
pinEcho = 18

print('Ultrasonic Measurement')

# set pins as Output and Input
GPIO.setup(pinTrigger, GPIO.OUT) # Trigger
GPIO.setup(pinEcho, GPIO.IN) # Echo

try:
    # Repeat the next indented block forever
    while True:
        # Set the trigger to False (low)
        GPIO.output(pinTrigger, False)
    
        # Allow module to settle
        time.sleep(0.5)

        # Send 10us pule to trigger
        GPIO.output(pinTrigger, True)
        time.sleep(0.00001)
        GPIO.output(pinTrigger, False)

       # Start the timer
        StartTime = time.time()

        # The start time is reset until the Echo pin is taken high (==1)
        while GPIO.input(pinEcho)==0:
            StartTime = time.time()

        # Stop when the Echo pin is no longer high - the end time
        while GPIO.input(pinEcho)==1:
            StopTime = time.time()
        # If the sensor is too close to an object, the PI cannot see
        # the echo quickly enough, so it has to detect that problem
        # and say what happened 
        if StopTime-StartTime >= 0.04:
            print('Hold on there! You are too close for me to see!')
            StopTime = StartTime
            break

        # Calculate pulse length
        ElapsedTime = StopTime - StartTime

        # Distance pulse travelled in that time is 
        # time mulpilied by the speed of sound (cm/s)
        Distance = ElapsedTime * 34326

        # That was the distance there and back so halve the value
        Distance = Distance  / 2

        print('Distance: %.1f cm' % Distance)

        time.sleep(0.5) 

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    # Reset GPIO settings
    GPIO.cleanup()
