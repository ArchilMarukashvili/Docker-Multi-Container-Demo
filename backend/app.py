from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # enable CORS for all routes

@app.route("/chess/<username>")
def chess_stats(username):
    url = f"https://api.chess.com/pub/player/{username}/stats"
    headers = {"User-Agent": "docker-demo-app/1.0"}
    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        return jsonify({"error": f"Failed to fetch data for {username}", "status": r.status_code}), r.status_code

    try:
        data = r.json()
    except Exception:
        return jsonify({"error": "Invalid JSON response"}), 500

    return jsonify(data)

@app.route("/api")
def api():
    return jsonify({"message": "Hello from backend"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
