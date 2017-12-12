from flask import Flask, request, render_template, redirect
from flask_mail import Mail, Message
from twilio.rest import Client
import sqlite3
import requests
from logIn import checkUser
from addaccount import addAccount
from newsapi import getnews
import json

app = Flask(__name__)

# Configurations for Flask Mail
app.config.update(
		DEBUG = True,
		MAIL_SERVER = 'smtp.gmail.com',
		MAIL_PORT = 465,
		MAIL_USE_SSL = True,
		MAIL_USERNAME = 'sendmejunkapp@gmail.com',
		MAIL_PASSWORD = 'CS196UIUC'
		)
mail = Mail(app)

app.static_folder = 'static' #This is the folder where all the CSS files should go

# Home page of website
@app.route("/index.html")
def mainpage():
	return render_template("index.html") #Mainpage html

# Home page of website
@app.route('/')
def mainpage2():
	return render_template("index.html")

# About page of website
@app.route('/about.html')
def about():
	return render_template('about.html')

# Contact Page endpoint
@app.route('/contact.html', methods=['POST', 'GET'])
def contact():
	if request.method == "GET":
		return render_template('contact.html')
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		message = request.form['message']
		send_mail(message, "Contact Us", ["sendmejunkapp@gmail.com"])
		return "Form Sent"

@app.route("/sendmail") # This endpoint will sned a mail with given body, subject, and an array of emails
def send_mail(body, subject, email):
	msg = Message(subject,
				sender="sendmejunkapp@gmail.com",
				recipients= email)
	msg.body = body
	mail.send(msg)
	return 'Mail Sent'

@app.route("/sendmsg", methods=['POST']) #Hard coded to send message to me each time bc free trial
def send_msg():
	account_sid = "AC603a3ae621f42b817033f1093cc96f2b" # Credentials idealy should be in another file
	auth_token = "e23ad2899fbf693a69b8b12d00ebab9d"
	client = Client(account_sid, auth_token)
	message = client.messages.create(
		"+16308158510",
		body='test',
		from_="+12242231011")
	return 'msg sent', message.sid

@app.route("/login.html", methods=['GET']) # GET requesting this enpoint will just render html
def login():
	return render_template('login.html')


@app.route("/login.html", methods=['POST']) #POST requesting this endpoint will check if the user is in the database and log them in
def checklogin():
	username = request.form['email']
	password = request.form['password']
	if checkUser(username, password):
		return redirect("http://127.0.0.1:5000/dashboard.html", code=302)
	return render_template('login.html')

@app.route("/dashboard.html", methods=['GET', 'POST']) #Loads the dashboard for the user
def dashboard():	
	if request.method == 'GET':
		return render_template('dashboard.html') #Change this file to 'dashboard.html' to show the CSS version

@app.route("/test/backend", methods=['GET']) # Endpoint for demonstration purposes that send emails and text messages to the emails in the database.
def test_backend():
	return render_template('dashboardsimple.html')

@app.route("/signup.html", methods=['GET', 'POST']) # From for making a new user
def data():
	if request.method == 'GET':
		return render_template('signup.html')
	elif request.method == 'POST':
		email = request.form['email']
		password = request.form['psw']
		checkpassword = request.form['psw-repeat']
		phone = request.form['phone']
		user = request.form["username"]
		firstname = request.form["firstname"]
		lastname = request.form["lastname"]
		if password == checkpassword:
			addAccount(firstname, lastname, user, password, email, phone)
			return "Account Created"
		else:
			return render_template('signup.html')

@app.route("/send/quote", methods=["POST"]) # POST requesting this endpoint will send quote of the day
def send_quote():
	dbase = sqlite3.connect('Accounts.db')
	cur = dbase.cursor()
	cur.execute("SELECT * FROM Accounts")
	rows = cur.fetchall()
	emails = []
	for row in rows:
		emails.append(row[5])
	r = requests.post("http://api.forismatic.com/api/1.0/", data={"method": "getQuote", "format" : "text", 'key': 111, "lang": 'en'})
	send_mail(r.text, "Quote of the Day", emails)
	return "Mail Sent"

@app.route("/send/news", methods=['POST']) # POST requesting this endpoint will send news headline to emails in database
def send_news():
	dbase = sqlite3.connect('Accounts.db')
	cur = dbase.cursor()
	cur.execute("SELECT * FROM Accounts")
	rows = cur.fetchall()
	emails = []
	for row in rows:
		emails.append(row[5])
	headline = getnews()
	send_mail(headline,"Daily Headline", emails)
	return "Emails Sent"

@app.route("/send/trumpquote", methods=['POST']) # POST requesting this endpoint will send a Trump Quote email
def send_trump_quote():
	dbase = sqlite3.connect('Accounts.db')
	cur = dbase.cursor()
	cur.execute("SELECT * FROM Accounts")
	rows = cur.fetchall()
	emails = []
	for row in rows:
		emails.append(row[5])
	r = requests.get("https://api.whatdoestrumpthink.com/api/v1/quotes/random")
	data = json.loads(r.text)
	quote = data["message"]
	send_mail(quote, "Daily Trump Quote", emails)
	return "Emails Sent"

@app.route("/send/message", methods=['POST']) # POST Requesting this endpoint will send a text message
def send_message():
	subject = request.form['subject']
	message = request.form['message']
	dbase = sqlite3.connect('Accounts.db')
	cur = dbase.cursor()
	cur.execute("SELECT * FROM Accounts")
	rows = cur.fetchall()
	emails = []
	for row in rows:
		emails.append(row[5])
	send_mail(message, subject, emails)
	return "email sent"

if __name__ == "__main__":
	app.run()
