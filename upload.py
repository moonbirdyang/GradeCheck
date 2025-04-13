from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

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
