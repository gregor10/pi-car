from flask import Flask, request, jsonify, render_template
from models.motor_driver import MotorDriver

app = Flask(__name__, template_folder="templates")

motor_driver = MotorDriver(20, 100)


@app.route("/api/change-movement", methods=["POST"])
def change_movement():
    direction = request.args.get("direction")
    print("Change dir to", direction)

    if direction == "forward":
        motor_driver.go_forward()
    elif direction == "backward":
        motor_driver.go_backward()
    elif direction == "left":
        motor_driver.go_left()
    elif direction == "right":
        motor_driver.go_right()
    elif direction == "stop":
        motor_driver.stop()

    return jsonify({"success": True})


@app.route("/")
def static_files():
    return render_template("index.html")
