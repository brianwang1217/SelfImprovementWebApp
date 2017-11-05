from flask import Flask, request, render_template
from flask_mail import Mail, Message
from twilio.rest import Client
import sqlite3

#Adds account to SQLite Database, doesn't work yet

'''
import hashlib
#hash_object = hashlib.sha1(b'Hello World')
#hex_dig = hash_object.hexdigest()
'''

def addaccount(first, last, username, password, email, phone):
    dbase = sqlite3.connect("Accounts (2).db")
    act = dbase.cursor()
    act.execute('SELECT * from AccountInfo WHERE USERNAME=username AND PASSWORD=password')
    if act.fetchall():
        act.execute("INSERT INTO Accountinfo (ID, FIRSTNAME, LAST, USERNAME, PASSWORD, EMAIL, PHONENUMBER) VALUES (?,?,?,?,?,?,?)", (100, first, last, username, password, email, phone))
        dbase.commit()
        dbase.close()
        return "Account Created"
    else:
        return "Account already exists"
    
