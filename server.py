from flask import Flask, jsonify, render_template
from models.motor_driver import MotorDriver

app = Flask(__name__, template_folder="templates")

motor_driver = MotorDriver(20, 100)


@app.route("/change-movement", methods=["POST"])
def change_movement():
    

@app.route("/")
def static_files():
    return render_template("index.html")
