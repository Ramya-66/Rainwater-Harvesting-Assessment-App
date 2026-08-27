from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "rainwater_secret_123"

# Dummy credentials
USER = {"username": "admin", "password": "1234"}

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", user=session.get("user"))

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if username == USER["username"] and password == USER["password"]:
        session["user"] = username
        return redirect(url_for("home"))
    else:
        return render_template("home.html", error="Invalid credentials", user=None)

@app.route("/calculator")
def calculator():
    if "user" not in session:
        return redirect(url_for("home"))
    return render_template("calculator.html", user=session.get("user"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
