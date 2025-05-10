from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route("/pv-news", methods=["GET"])
def get_news():
    try:
        with open(os.path.join("data", "news.json"), "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
