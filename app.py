from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

fortunes = [
    "You will have a day full of unexpected surprises.",
    "Happiness is around the corner – keep smiling!",
    "An opportunity will soon knock on your door.",
    "Good news will come to you by mail.",
    "Adventure awaits you this weekend.",
    "Your hard work will soon pay off.",
    "A new friendship will bring joy to your life."
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fortune", methods=["POST"])
def fortune():
    name = request.json.get("name")
    fortune = f"{name}, your fortune is: {random.choice(fortunes)}"
    return jsonify({"fortune": fortune})
    
if __name__ == "__main__":
    app.run(debug=True)
