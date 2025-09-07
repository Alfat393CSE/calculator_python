from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    expression = ""

    if request.method == "POST":
        expression = request.form.get("expression")
        try:
            # Safely evaluate only arithmetic expressions
            result = eval(expression, {"__builtins__": None}, {})
        except Exception:
            result = "Error"

    return render_template("calculator.html", result=result, expression=expression)

if __name__ == "__main__":
    app.run(debug=True)
