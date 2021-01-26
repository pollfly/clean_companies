from company_database_functions import lookup_comp
from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)

# P.Z: maybe it will be prettier to saparate it to two different functions and remove the if.
# @app.route("/", methods=["POST"])
# def home_post():
#   comp = request.form["company"]
#   return redirect(url_for("company_check", myCompany=comp))
#
# @app.route("/", methods=["GET"])
# def home2_get():
#   return render_template("home.html")

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        comp = request.form["company"]
        return redirect(url_for("company_check", myCompany=comp))
    else:
        return render_template("home.html")

@app.route("/<myCompany>")
def company_check(myCompany):
    return render_template("results.html", message=lookup_comp(myCompany))


if __name__ == "__main__":
    app.run(debug=True)
