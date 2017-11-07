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

def addAccount(first, last, user, password, userEmail, phone):
    dbase = sqlite3.connect("Accounts.db")
    act = dbase.cursor()
    #act.execute('SELECT * from Accounts WHERE USERNAME=username AND PASSWORD=password')

    row = (100, first, last, user, password, userEmail, phone)
    if (not act.execute("SELECT * FROM Accounts WHERE USERNAME=?",(format(user),)).fetchone()[0] or not act.execute("SELECT * FROM Accounts WHERE EMAIL=?",(format(userEmail),)).fetchone()[0]):
        act.execute("INSERT INTO Accounts (ID, FIRSTNAME, LASTNAME, USERNAME, PASSWORD, EMAIL, PHONENUMBER) VALUES (?,?,?,?,?,?,?)", row)
        dbase.commit()
        dbase.close()
        print ("account made");
        return True
    else:
    	print ("account exists");
    	return False
    
