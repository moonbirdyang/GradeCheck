from flask import Flask, request, render_template
from flask import jsonify
import os
import csv

app = Flask(__name__)

students = {
    "小明": 88,
    "小華": 92,
    "小美": 75
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    name = request.form["name"]
    score = students.get(name)
    return render_template("result.html", name=name, score=score)

@app.route("/upload", methods=["POST"])
def upload_data():
    data = request.json
    if not data:
        return jsonify({"status": "fail", "msg": "No data received"}), 400

    try:
        with open("students_data.csv", "w", newline='', encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "score", "note"])
            for item in data:
                writer.writerow([item["name"], item["score"], item["note"]])
        return jsonify({"status": "success", "msg": "資料成功上傳！"})
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # 在 Railway 會提供 PORT，否則預設 5000
    app.run(host="0.0.0.0", port=port)
