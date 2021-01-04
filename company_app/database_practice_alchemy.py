from company_app.flask_practice import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.company_database'
# 3 slashes = relative path
# 4 slashes = absolute
db = SQLAlchemy(app)

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    type = db.Column(db.String(30))
    year =db.Column(db.Integer)
    location = db.Column(db.String(50))
    history = db.Column(db.String(600))

    def __repr__(self):
        return '<User %r>' % self.username

db.create_all()

nike = Company(name="Nike", type="Textiles", year=1930, location="New York", history="child labor")
adidas = Company(name="Adidas", type="Textiles", year=1920, location="San Francisco", history="...cannibalism?")
db.session.add(adidas)
db.session.add(nike)
db.session.commit()