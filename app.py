from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String, Float
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir,'planets.db')

db = SQLAlchemy(app)
@app.route("/",methods=['GET'])
def hello_world():
    return jsonify({"name":"Rita"}),200

@app.route("/error")
def print_error():
    return jsonify({"message":"there is an error"}),400


@app.route("/params")
def print_params():
    return jsonify({"name":request.args.get('name')}),200

@app.route("/about/<string:username>")
def about_page(username:str):
    return f"<h1>About {username}</h1>"

# database models
class User(db.Model):
    __tablename__ = 'users'
    id= Column(Integer,primary_key=True)
    first_name=Column(String)
    last_name=Column(String)
    email=Column(String, unique=True)
    password=Column(String)

if __name__ =='__main__':
    app.run(debug=True)