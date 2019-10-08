from flask import Flask, render_template,request,redirect,url_for
import pymysql

app = Flask(__name__)


#rendering the different page
@app.route("/")  
def home():   
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/home")
def home1():
    return render_template("index.html")






#taking the signup data
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

#taking the login data
@app.route("/action_login", methods = ["Post"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    print(username,password)
    #check_validation(username)
    return render_template("index.html")




app.run(debug=True)
