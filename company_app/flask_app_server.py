from company_database_functions import lookup_company
from flask import Flask, redirect, render_template, request, url_for
import sqlite3
import config
from company_database_functions import get_all_companies_info
app = Flask(__name__)


@app.route("/", methods=["POST"])
def home_post():
    comp = request.form["company"]
    return redirect(url_for("company_check", my_company=comp))


@app.route("/", methods=["GET"])
def home2_get():
    return render_template("home.html")


@app.route("/<my_company>")
def company_check(my_company):
    return render_template("results.html", message=lookup_company(my_company))


def listify_alphabetize_company_info():
    data = get_all_companies_info(history=False)
    list_data = [list(i) for i in data]
    list_data.sort(key=lambda x: x[0].lower())
    return list_data


def link_first_column(company_data_list):
    for row in company_data_list:
        row[0] = f"<a href='/{row[0]}'>{row[0]}</a>"
    return company_data_list


@app.route("/company_table")
def table():
    headings = ("Company", "Location", "Products")
    return render_template("all_companies.html", headings=headings,
                           data=link_first_column((listify_alphabetize_company_info())))


@app.route("/more_info")
def more_info():
    pass


if __name__ == "__main__":
    app.run(debug=True)
