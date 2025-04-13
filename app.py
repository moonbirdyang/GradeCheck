from flask import Flask, request, render_template

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
    app.run(debug=True)
