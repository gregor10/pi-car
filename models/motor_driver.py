NO_MODULE = False
try:
    import RPi.GPIO as gpio
except Exception as ex:
    NO_MODULE = True


import time

MOTOR_A_FORWARD_PIN = 17
MOTOR_A_BACKWARD_PIN = 22
MOTOR_B_FORWARD_PIN = 23
MOTOR_B_BACKWARD_PIN = 24


class MotorDriver:
    def __init__(self, speed, max_speed):
        self.motor_A_forward = None
        self.motor_A_backward = None
        self.motor_B_forward = None
        self.motor_B_backward = None

        self.motor_speed = speed
        self.max_speed = max_speed

        if not NO_MODULE:
            self.init_pins()

    def __del__(self):
        self.stop()
        gpio.cleanup()

    def init_pins(self):
        gpio.setmode(gpio.BCM)

        gpio.setup(MOTOR_A_FORWARD_PIN, gpio.OUT)
        gpio.setup(MOTOR_A_BACKWARD_PIN, gpio.OUT)
        gpio.setup(MOTOR_B_FORWARD_PIN, gpio.OUT)
        gpio.setup(MOTOR_B_BACKWARD_PIN, gpio.OUT)

        self.motor_A_forward = gpio.PWM(MOTOR_A_FORWARD_PIN, self.max_speed)
        self.motor_A_forward.start(0)
        self.motor_A_backward = gpio.PWM(MOTOR_A_BACKWARD_PIN, self.max_speed)
        self.motor_A_backward.start(0)

        self.motor_B_forward = gpio.PWM(MOTOR_B_FORWARD_PIN, self.max_speed)
        self.motor_B_forward.start(0)
        self.motor_B_backward = gpio.PWM(MOTOR_B_BACKWARD_PIN, self.max_speed)
        self.motor_B_backward.start(0)

    def set_speed(self, speed):
        self.stop()
        self.motor_speed = speed
    
    def get_speed(self):
        return self.motor_speed

    def stop(self):
        self.motor_A_forward.start(0)
        self.motor_A_backward.start(0)

        self.motor_B_forward.start(0)
        self.motor_B_backward.start(0)

    def go_forward(self):
        self.motor_A_forward.start(self.motor_speed)
        self.motor_A_backward.start(0)

        self.motor_B_forward.start(self.motor_speed)
        self.motor_B_backward.start(0)

    def go_backward(self):
        self.motor_A_forward.start(0)
        self.motor_A_backward.start(self.motor_speed)

        self.motor_B_forward.start(0)
        self.motor_B_backward.start(self.motor_speed)

    def go_forward_right(self):
        self.motor_A_forward.start(self.motor_speed)
        self.motor_A_backward.start(0)

        self.motor_B_forward.start(0)
        self.motor_B_backward.start(0)
    
    def go_forward_left(self):
        self.motor_A_forward.start(0)
        self.motor_A_backward.start(0)

        self.motor_B_forward.start(self.motor_speed)
        self.motor_B_backward.start(0)
    
    def go_backward_left(self):
        self.motor_A_forward.start(0)
        self.motor_A_backward.start(0)

        self.motor_B_forward.start(0)
        self.motor_B_backward.start(self.motor_speed)

    def go_backward_right(self):
        self.motor_A_forward.start(0)
        self.motor_A_backward.start(self.motor_speed)

        self.motor_B_forward.start(0)
        self.motor_B_backward.start(0)

    def go_right(self):
        self.motor_A_forward.start(self.motor_speed)
        self.motor_A_backward.start(0)

        self.motor_B_forward.start(0)
        self.motor_B_backward.start(self.motor_speed)

    def go_left(self):
        self.motor_A_forward.start(0)
        self.motor_A_backward.start(self.motor_speed)

        self.motor_B_forward.start(self.motor_speed)
        self.motor_B_backward.start(0)


# print("---Test---")
# motor_driver = MotorDriver(90, 100)

# motor_driver.go_forward()
# time.sleep(6)
# motor_driver.stop()

# motor_driver.go_backward()
# time.sleep(6)
# motor_driver.stop()

# motor_driver.go_left()
# time.sleep(6)
# motor_driver.stop()

# motor_driver.go_right()
# time.sleep(6)
# motor_driver.stop()
