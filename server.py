
from flask import Flask, request, jsonify, render_template, copy_current_request_context
from flask_socketio import SocketIO, emit
from models.motor_driver import MotorDriver
from models.servo_motor import ServoDriver
from models.ultrasonic import UltrasonicModule

from threading import Thread
import time
import os

app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] = "30_TISHI_PATARA_FULIA?"
socketio = SocketIO(app)


@app.after_request
def add_header(response):
    response.cache_control.max_age = 5
    return response


motor_driver = MotorDriver(75, 100)
servo_driver = ServoDriver()
ultrasonic_driver = UltrasonicModule()


@socketio.on("connection_identification_event")
def handle_connection_identification_event(json):
    print("received json: " + str(json), '\n\n')

    @copy_current_request_context
    def get_ultrasonic_distance():
        while True:
            distance = ultrasonic_driver.get_distance()
            time.sleep(0.15)
            if distance < 15.0:
                os.system("mpg123 /home/pi/Music/obstacle.mp3")

            emit('ultrasonic_distance', {"distance": distance})

    Thread(target=get_ultrasonic_distance).start()


@socketio.on("change_direction")
def handle_change_direction_event(json):
    print("Change direction:", json)

    if "direction" in json:
        if json["direction"] == "forward":
            motor_driver.go_forward()
        elif json["direction"] == "forward_left":
            motor_driver.go_forward_left()
        elif json["direction"] == "forward_right":
            motor_driver.go_forward_right()
        elif json["direction"] == "backward":
            motor_driver.go_backward()
        elif json["direction"] == "backward_left":
            motor_driver.go_backward_left()
        elif json["direction"] == "backward_right":
            motor_driver.go_backward_right()
        elif json["direction"] == "left":
            motor_driver.go_left()
        elif json["direction"] == "right":
            motor_driver.go_right()
        elif json["direction"] == "stop":
            motor_driver.stop()


@socketio.on("change_camera_angle")
def handle_change_camera_angle(json):
    print("Change angle:", json)

    if "angle" in json:
        servo_driver.rotate_camera(angle=json["angle"])


@socketio.on('disconnect')
def handle_disconnect_event():
    print('Client disconnected')


@app.route("/")
def static_files():
    return render_template("index.html")
