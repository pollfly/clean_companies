from company_database_functions import lookup_company
from flask import Flask, redirect, render_template, request, url_for
import sqlite3


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

@app.route("/", methods=["POST"])
def home_post():
  comp = request.form["company"]
  return redirect(url_for("company_check", myCompany=comp))


@app.route("/", methods=["GET"])
def home2_get():
  return render_template("home.html")

@app.route("/<myCompany>")
def company_check(myCompany):
    return render_template("results.html", message=lookup_company(myCompany))


headings = ("Company", "Location", "Products")
conn1 = sqlite3.connect('../company.db')
c = conn1.cursor()
c.execute("SELECT name, country_founded, products FROM companies")
data = list(c.fetchall())
list_data = [list(i) for i in data]
for row in list_data:
    row[0] = f"<a href='/{row[0]}'>{row[0]}</a>"

conn1.close()

@app.route("/company_table")
def table():
    return render_template("all_companies.html", headings=headings, data=list_data)


if __name__ == "__main__":
    app.run(debug=True)
