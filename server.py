
from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO
from models.motor_driver import MotorDriver

app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] = "30_TISHI_PATARA_FULIA?"
socketio = SocketIO(app)


@app.after_request
def add_header(response):
    response.cache_control.max_age = 5
    return response


motor_driver = MotorDriver(75, 100)

@socketio.on("connection_identification_event")
def handle_connection_identification_event(json):
    print("received json: " + str(json))


@socketio.on("change_direction")
def change_direction(json):
    print("Change direction:", json)

    if "direction" in json:
        if json["direction"] == "forward":
            motor_driver.go_forward()


# @app.route("/api/change-movement", methods=["POST"])
# def change_movement():
#     direction = request.args.get("direction")
#     print("Change dir to", direction)

#     if direction == "forward":
#         motor_driver.go_forward()
#     elif direction == "backward":
#         motor_driver.go_backward()
#     elif direction == "left":
#         motor_driver.go_left()
#     elif direction == "right":
#         motor_driver.go_right()
#     elif direction == "stop":
#         motor_driver.stop()

#     return jsonify({"success": True})


@app.route("/")
def static_files():
    return render_template("index.html")
