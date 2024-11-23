from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import requests

app = Flask(__name__)

api_keys = {
    "brad": "27/11/2024",
    "por": "27/11/2024",
    "grimgo": "30/12/2025"}

def is_key_valid(key):
    return key in api_keys and datetime.utcnow() <= datetime.strptime(api_keys[key], "%d/%m/%Y")

@app.route("/ff.Likes", methods=["GET"])
def send_likes():
    uid = request.args.get("uid")
    if not is_key_valid(request.args.get("r")): return "key đã hết hạn"
    if not uid: return jsonify({"error": "?"}), 400

    api_url = f"https://likesapi-ff.onrender.com/Likes?uid={uid}"
    try:
        response = requests.get(api_url)
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return "error something"

if __name__ == "__main__":
    app.run(debug=True)
