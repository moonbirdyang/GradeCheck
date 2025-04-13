from flask import Flask, request, render_template
from flask import jsonify
import os
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return "這是首頁，目前沒有搜尋功能。"

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
    
@app.route("/data")
def show_data():
    students = []
    try:
        with open("students_data.csv", newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        return "目前尚無資料。"

    return render_template("data.html", students=students)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # 在 Railway 會提供 PORT，否則預設 5000
    app.run(host="0.0.0.0", port=port)
