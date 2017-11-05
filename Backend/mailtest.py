from flask import Flask, request, render_template
from flask_mail import Mail, Message
from twilio.rest import Client
import sqlite3

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
def send_mail():
	msg = Message("Test",
				sender="sendmejunkapp@gmail.com",
				recipients=["talk2shreyas@gmail.com"])
	msg.body = "Test"
	mail.send(msg)
	return 'Mail Sent'

@app.route("/sendmsg/")
def send_msg():
	account_sid = "AC603a3ae621f42b817033f1093cc96f2b"
	auth_token = "e23ad2899fbf693a69b8b12d00ebab9d"
	client = Client(account_sid, auth_token)
	message = client.messages.create(
        "+16308158510",
        body="Test",
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

if __name__ == "__main__":
	app.run()
