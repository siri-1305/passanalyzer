from flask import Flask, render_template, request, jsonify
from utils.password_checker import analyze_password
from utils.generator import generate_password
from utils.breach_check import check_breach

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    password = request.json["password"]

    result = analyze_password(password)
    breach = check_breach(password)

    result["breached"] = breach

    return jsonify(result)


@app.route("/generate")
def generate():
    password = generate_password()
    return jsonify({"password": password})


if __name__ == "__main__":
    app.run(debug=True)
