from flask import Flask, render_template, request, flash

app = Flask(__name__)  # creats a class for our app
app.secret_key = "manbarpig_MUDMAN888"

#select a route for this app
@app.route("/hello") # example myapp.com/hello
def index():
	flash("what is your name?")
	return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
	flash("Hi " + str(request.form["name_input"]) + ". It's great to see you!")
	return render_template("index.html")

