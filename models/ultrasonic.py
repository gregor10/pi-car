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
    def __init__(self, max_distance_between_obstacle=15):
        # use Raspberry Pi board pin numbers
        if not NO_MODULE:
            self.max_distance_between_obstacle = max_distance_between_obstacle

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

        # print("Distance: %.1f cm" % distance)
        return distance

    def should_stop(self, count=0):
        if count == 3:
            return True

        distance = self.get_distance()
        if distance <= self.max_distance_between_obstacle:
            return self.should_stop(count=count+1)

        return False


# ultrasonic = UltrasonicModule(max_distance_between_obstacle=15)
# while True:
#    should_stop = ultrasonic.should_stop()
#    print('should_stop', should_stop, '\n')
#    # time.sleep(1)
