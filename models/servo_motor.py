NO_MODULE = False
try:
    import RPi.GPIO as GPIO
except Exception as ex:
    NO_MODULE = True

SERVO_PWM_PIN = 7


class ServoDriver:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(SERVO_PWM_PIN, GPIO.OUT)
        self.servo = GPIO.PWM(SERVO_PWM_PIN, 50)

    def __del__(self):
        """Stop servo"""
        self.servo.stop()
        GPIO.cleanup()

    def rotate_camera(self, angle):
        """Rotate camera --- angle (0, 90, 180)"""
        if angle == 90:
            self.servo.ChangeDutyCycle(7.5)  # turn towards 90 deg
            print('turned 90deg')
        elif angle == 0:
            self.servo.ChangeDutyCycle(2.5)  # 0 deg
            print('turned 0deg')
        elif angle == 180:
            self.servo.ChangeDutyCycle(12.5)  # 180 deg
            print('turned 180deg')
