from flask import Flask, request, render_template
from flask_mail import Mail, Message
from twilio.rest import Client
import sqlite3
import requests
from logIn import checkUser
from addaccount import addAccount

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

app.static_folder = 'static' #This is the folder where all the CSS files should go

@app.route("/")
def mainpage():
	return render_template("index.html") #Mainpage html

@app.route("/sendmail/") # This endpoint will sned a mail with given body, subject, and an array of emails
def send_mail(body, subject, email):
	msg = Message(subject,
				sender="sendmejunkapp@gmail.com",
				recipients= [email])
	msg.body = body
	mail.send(msg)
	return 'Mail Sent'

@app.route("/sendmsg/<input>") #Hard coded to send message to me each time bc free trial
def send_msg(message):
	account_sid = "AC603a3ae621f42b817033f1093cc96f2b"
	auth_token = "e23ad2899fbf693a69b8b12d00ebab9d"
	client = Client(account_sid, auth_token)
	message = client.messages.create(
        "+16308158510",
        body=message,
        from_="+12242231011")
	return 'msg sent', message.sid

@app.route("/login.html", methods=['GET']) # POST this endpoint with 
def login():
	return render_template('login.html')
	
@app.route("/login.html", methods=['GET'])
def checklogin():
    # This is if you are giving backend the information through the forms
	username = request.form("email")
	password = request.form("password")
	The below is if you are POSTing the backend with a Json
	json_dict = json.loads(request.data)
	username = json_dict['username']
	password = jsondict['password']
	if checkUser(username, password):
		return redirect("http://127.0.0.1:5000/dashboard.html", code=302)
	return "Login Failed"

@app.route("/dashboard.html")
def dashboard():
    return render_template()
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
