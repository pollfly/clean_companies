from flask import Flask, render_template
from company_database_functions import lookup_comp

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/check_company/<myCompany>")
def company_check(myCompany):
    return lookup_comp(myCompany)

if __name__ == "__main__":
    app.run(debug=True)