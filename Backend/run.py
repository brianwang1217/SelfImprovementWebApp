from flask import Flask, request, render_template
from flask_mail import Mail, Message
from twilio.rest import Client
import sqlite3
import addaccount
app = Flask(__name__)

#Main function that should contain all our endpoints at the end

@app.route("/")
def hello():
    return "Self Improvement App"

@app.route("/signup", methods=['GET', 'POST'])
def loginpage():
    return render_template('index.html')

@app.route("/signup-success", methods=['GET', 'POST'])
def loginsuccess():
    user = request.form.get("username")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm-password")

    if password == confirm_password:
        addaccount("first", "last", user, password, "email", 999999999)
        return "Account Created"
    else:
        return "Passwords don't match"

@app.route("/about.html", methods=['GET', 'POST'])
def aboutpage():
    return render_template('about.html')

@app.route("/about.html", methods=['GET', 'POST'])
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
