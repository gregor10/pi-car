NO_MODULE = False
try:
    import RPi.GPIO as GPIO
except Exception as ex:
    NO_MODULE = True
import time
import signal
import sys

PIN_TRIGGER = 18
PIN_ECHO = 21


class UltrasonicModule:
    def __init__(self):
        # use Raspberry Pi board pin numbers
        if not NO_MODULE:
            GPIO.setmode(GPIO.BCM)
            self.pin_trigger = PIN_TRIGGER
            self.pin_echo = PIN_ECHO
            GPIO.setup(PIN_TRIGGER, GPIO.OUT)
            GPIO.setup(PIN_ECHO, GPIO.IN)

    def __del__(self):
        print("\nTurning off ultrasonic distance detection...\n")
        GPIO.cleanup()

    def get_distance(self):
         # set Trigger to HIGH
        GPIO.output(self.pin_trigger, True)
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.pin_trigger, False)

        startTime = time.time()
        stopTime = time.time()

        # save start time
        while 0 == GPIO.input(self.pin_echo):
            startTime = time.time()

        # save time of arrival
        while 1 == GPIO.input(self.pin_echo):
            stopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = stopTime - startTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        print("Distance: %.1f cm" % distance)
        return distance


distance_detector = UltrasonicModule()
while True:
    curr_distance = distance_detector.get_distance()
    print('curr_distance', curr_distance)
    # time.sleep(1)
    
