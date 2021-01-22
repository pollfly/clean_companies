from flask import Flask, redirect, url_for, request, redirect, render_template
from company_database_functions import lookup_comp
from flask_wtf import FlaskForm
from wtforms import StringField, validators

app = Flask(__name__)


@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        comp = request.form["company"]
        return redirect(url_for("company_check", myCompany=comp))
    else:
        return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/<myCompany>")
def company_check(myCompany):
    return lookup_comp(myCompany) + "<br> <form action='/'> <input type='submit' value='Return to Home'/></form>"

if __name__ == "__main__":
    app.run(debug=True)