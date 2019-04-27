
from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO, emit
from models.motor_driver import MotorDriver
from models.servo_motor import ServoDriver

from threading import Thread
import time

app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] = "30_TISHI_PATARA_FULIA?"
socketio = SocketIO(app)


@app.after_request
def add_header(response):
    response.cache_control.max_age = 5
    return response


motor_driver = MotorDriver(75, 100)
servo_driver = ServoDriver()


def test():
    while True:
        time.sleep(1)
        emit('ultrasonic_distance', {"distance": 2.0})


@socketio.on("connection_identification_event")
def handle_connection_identification_event(json):
    print("received json: " + str(json))
    thread = Thread(target=test, args=())
    thread.start()


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
