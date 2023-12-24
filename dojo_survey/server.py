from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "keepitsecretkeepitsafe"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form.get("name")
    location = request.form.get("location")
    language = request.form.get("language")
    comment = request.form.get("comment")

    session["name"] = name
    session["location"] = location
    session["language"] = language
    session["comment"] = comment

    return render_template(
        "result.html", name=name, location=location, language=language, comment=comment
    )


@app.route("/result")
def result():
    name = session.get("name")
    location = session.get("location")
    language = session.get("language")
    comment = session.get("comment")
    return render_template(
        "result.html", name=name, location=location, language=language, comment=comment
    )


if __name__ == "__main__":
    app.run(debug=True)
