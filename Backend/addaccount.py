#from flask import Flask, request, render_template
#from flask_mail import Mail, Message
#from twilio.rest import Client
import sqlite3

#Adds account to SQLite Database, doesn't work yet

'''
import hashlib
#hash_object = hashlib.sha1(b'Hello World')
#hex_dig = hash_object.hexdigest()
'''

def addAccount(first, last, user, password, passwordCheck, userEmail, phone):
    dbase = sqlite3.connect("Accounts.db")
    act = dbase.cursor()
    #act.execute('SELECT * from Accounts WHERE USERNAME=username AND PASSWORD=password')

    row = (first, last, user, password, userEmail, phone)
    act.execute("SELECT * FROM Accounts WHERE USERNAME=?",(format(user),))
    userExist = act.fetchone()

    act.execute("SELECT * FROM Accounts WHERE EMAIL=?",(format(userEmail),))
    emailExist = act.fetchone()
    if password is not passwordCheck:
        print("passwords do not match")
        return False
    if (userExist is not None): #act.execute("SELECT * FROM Accounts WHERE USERNAME=?",(format(user),)).fetchone()[0]
    	print ("username taken");
    	return False
    elif (emailExist is not None): #not act.execute("SELECT * FROM Accounts WHERE EMAIL=?",(format(userEmail),)).fetchone()[0]
    	print ("email taken!");
    	return False
    else:
    	act.execute("INSERT INTO Accounts ( FIRSTNAME, LASTNAME, USERNAME, PASSWORD, EMAIL, PHONENUMBER) VALUES (?,?,?,?,?,?)", row)
    	dbase.commit()
    	dbase.close()
    	print("account made");
    	return True
