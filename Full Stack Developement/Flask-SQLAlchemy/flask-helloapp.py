from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@127.0.0.1:5432/example'
db  = SQLAlchemy(app) # database

class Person(db.Model): 
# don't need to define an init method because SQLAlchemy does it for you when you use it in a class
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), nullable = False)

db.create_all()

@app.route('/')
def index():
    return "Hello World!"
if __name__ == '__main__':
    app.run(debug = True)