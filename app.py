from flask import Flask, request, render_template
import os

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # 在 Railway 會提供 PORT，否則預設 5000
    app.run(host="0.0.0.0", port=port)
