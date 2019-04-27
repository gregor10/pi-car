import random
import time

from models.ultrasonic import UltrasonicModule
from models.motor_driver import MotorDriver

MAX_DISTANCE_BETWEEN_OBSTACLE = 15

MOTORS_SPEED = 60
MAX_SPEED = 100


class ObstacleAvoider:
    def __init__(self):
        self.ultrasonic_driver = UltrasonicModule(
            max_distance_between_obstacle=MAX_DISTANCE_BETWEEN_OBSTACLE)

        self.motor_driver = MotorDriver(
            speed=MOTORS_SPEED, max_speed=MAX_SPEED)

    def avoid_obstacles(self):
        while True:
            should_stop = self.ultrasonic_driver.should_stop()
            print('should_stop', should_stop, '\n')
            if should_stop:
                self.motor_driver.stop()
                time.sleep(1)
                self.motor_driver.go_backward()
                time.sleep(1)

                random_int = random.randint(0, 1)

                if random_int == 1:
                    self.motor_driver.go_right()
                else:
                    self.motor_driver.go_left()
                time.sleep(0.5)
                self.motor_driver.stop()
                time.sleep(1)
            else:
                self.motor_driver.go_forward()

obstacle_avoider = ObstacleAvoider()
obstacle_avoider.avoid_obstacles()
