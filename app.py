from flask import Flask, request, jsonify
import string, secrets, random

app = Flask(__name__)

@app.post("/generate")
def generate():
    data = request.json
    length = int(data["length"])

    chars = ""
    if data["upper"]: chars += string.ascii_uppercase
    if data["lower"]: chars += string.ascii_lowercase
    if data["digits"]: chars += string.digits
    if data["special"]: chars += "!@#$%^&*"

    if not chars:
        return jsonify({"password": ""})

    # ensure at least one from each selected type
    password = []
    if data["upper"]: password.append(secrets.choice(string.ascii_uppercase))
    if data["lower"]: password.append(secrets.choice(string.ascii_lowercase))
    if data["digits"]: password.append(secrets.choice(string.digits))
    if data["special"]: password.append(secrets.choice("!@#$%^&*"))

    # fill the rest
    while len(password) < length:
        password.append(secrets.choice(chars))

    random.shuffle(password)
    return jsonify({"password": "".join(password)})

app.run(host="0.0.0.0", port=5000)
