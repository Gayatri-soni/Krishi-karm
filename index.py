from flask import Flask, render_template,request,redirect
import pymysql

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")
    return render_template("contact.html")
    return render_template("about.html")


@app.route("/action_signup",   methods = ["GET","POST"])
def sign_up():
    name = request.form.get("name")
    state=request.form.get("state")
    city= request.form.get("city")
    Aadhaar = request.form.get("Aadhaar")
    mobile = request.form.get("mobile")
    address=request.form.get("address")
    print(name,state,city, Aadhaar,mobile,address)
    #insert(name, aadhaar, mob)
    return render_template("index.html")


@app.route("/action_login", methods = ["Post"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    print(username,password)
    #check_validation(username)
    return render_template("index.html")




app.run(debug=True)