from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 + num2
        return render_template("home.html", result=result)
    else:
        return render_template("home.html")


if __name__ == "__main__":
    app.run()
