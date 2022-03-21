from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    operations = ["add", "subtract", "multiply", "divide"]
    return render_template("home.html", operations=operations)


@app.route("/<string:operation>")
def operate(operation):
    return render_template(f"{operation}.html", operation_type=operation)


@app.route("/result/<string:operation>", methods=["GET", "POST"])
def getresult(operation):
    if request.method == "POST":
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        else:
            result = round(num1 / num2, 2)
        return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
