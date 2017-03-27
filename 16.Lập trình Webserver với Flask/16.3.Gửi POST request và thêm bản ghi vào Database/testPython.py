from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request

app = Flask("__name_")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://hoangnd:123456@localhost:5432/postgresdemo'
db = SQLAlchemy(app)

class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False)
    age = db.Column(db.Integer, unique=False)

    def __init__(self, name, age):
        self.name = name
        self.age = age

@app.route('/insert_cat', methods=['POST'])
def insertCat():
    name = request.form['name']
    age = request.form['age']
    newCat = Cat(name, age)
    db.session.add(newCat)
    db.session.commit()
    return "<h1>New cat is inserted</h1>"

if __name__ == '__main__':
    app.run()

