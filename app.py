from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    expression = ""

    if request.method == "POST":
        expression = request.form.get("expression")
        try:
            # allow safe math functions
            allowed = {
                "sqrt": math.sqrt,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "log": math.log,
                "pi": math.pi,
                "e": math.e
            }
            result = eval(expression, {"__builtins__": None}, allowed)
        except Exception:
            result = "Error"

    return render_template("calculator.html", result=result, expression=expression)

if __name__ == "__main__":
    app.run(debug=True)
