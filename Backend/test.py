from flask import Flask, request, render_template
from flask_mail import Mail, Message
from twilio.rest import Client
import sqlite3

def send_msg():
    	account_sid = "AC603a3ae621f42b817033f1093cc96f2b"
	auth_token = "e23ad2899fbf693a69b8b12d00ebab9d"
	client = Client(account_sid, auth_token)
	message = client.messages.create(
        "+16308158510",
        body="Test",
        from_="+12242231011")
	return 'msg sent', message.sid