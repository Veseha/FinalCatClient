from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("rooms.html", title="каюты")


app.run(port=8080, host="127.0.0.1")
