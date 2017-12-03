from flask import Flask, request, render_template
from flask_mail import Mail, Message
from twilio.rest import Client
import sqlite3
import requests


#This file experiments with some endpoints and the send mail and send msg APIs

app = Flask(__name__)


app.config.update(
		DEBUG = True,
		MAIL_SERVER = 'smtp.gmail.com',
		MAIL_PORT = 465,
		MAIL_USE_SSL = True,
		MAIL_USERNAME = 'sendmejunkapp@gmail.com',
		MAIL_PASSWORD = 'CS196UIUC'
		)
mail = Mail(app)

app.static_folder = 'static'

@app.route("/")
def mainpage():
	return render_template("index.html")

@app.route("/sendmail/")
def send_mail(body, subject, email):
	msg = Message(subject,
				sender="sendmejunkapp@gmail.com",
				recipients= [email])
	msg.body = body
	mail.send(msg)
	return 'Mail Sent'

@app.route("/sendmsg/<input>")
def send_msg(input):
	account_sid = "AC603a3ae621f42b817033f1093cc96f2b"
	auth_token = "e23ad2899fbf693a69b8b12d00ebab9d"
	client = Client(account_sid, auth_token)
	message = client.messages.create(
        "+16308158510",
        body=input,
        from_="+12242231011")
	return 'msg sent', message.sid

@app.route("/login", methods=['GET', 'POST'])
def login():
	return render_template('index.html')
	
@app.route("/login-success", methods=['GET', 'POST'])
def checklogin():
	data = request.form.get("username")
	return data

@app.route("/signup")
def data():
	return render_template('signup_page.html')

@app.route("/send/quote")
def send_quote():
	dbase = sqlite3.connect('Accounts.db')
	cur = dbase.cursor()
	cur.execute("SELECT * FROM Accounts")
	rows = cur.fetchall()
	emails = []
	for row in rows:
		numbers.append(row[6])
	for row in rows:
		emails.append(row[5])
	r = requests.post("http://api.forismatic.com/api/1.0/", data={"method": "getQuote", "format" : "text", 'key': 111, "lang": 'en'})
	for email in emails:
		send_mail(r.text, "Quote of the Day", email)
	send_msg(r.text)
	return "done"


if __name__ == "__main__":
	app.run()
