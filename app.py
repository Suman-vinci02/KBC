# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

Questions = [
    "Who is Sachin Tendulkar?",
    "Who is Messi?",
    "What is the capital of India?"
]

Options = [
    ["1. Footballer", "2. Cricketer", "3. Table Tennis Player", "4. Chess Player"],
    ["1. Footballer", "2. Cricketer", "3. Table Tennis Player", "4. Chess Player"],
    ["1. Kolkata", "2. Delhi", "3. Mumbai", "4. Bengaluru"]
]

Answers = [2, 1, 2]
Prizes = [1000, 5000, 20000]

total = 0
q_index = 0

@app.route("/", methods=["GET", "POST"])
def quiz():
    global total, q_index
    message = ""
    if request.method == "POST":
        ans = int(request.form.get("answer"))
        if ans == Answers[q_index]:
            total += Prizes[q_index]
            message = f"Correct! You won ₹{Prizes[q_index]}!"
            q_index += 1
            if q_index == len(Questions):
                return render_template("result.html", total=total)
        else:
            message = "Wrong Answer!"
            return render_template("result.html", total=total)

    return render_template(
        "quiz.html",
        question=Questions[q_index],
        options=Options[q_index],
        total=total,
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)
