#!/usr/bin/python

import sqlite3

def insertAccount(ID, firstName, lastName, username, password, email, phoneNumber):
	dbase = sqlite3.connect('Accounts.db')
	act = dbase.cursor()
	act.execute("INSERT INTO Accounts VALUES (userID, first, lastName, user, userPassword, userEmail, userPhoneNumber)")
	dbase.commit()
	dbase.close()

def retrieveUser(user):
 	dbase = sqlite3.connect('Accounts.db')
	act = dbase.cursor()
	act.execute("SELECT ID, FIRSTNAME, LAST, USERNAME, PASSWORD, EMAIL, PHONENUMBER FROM AccountInfo WHERE USERNAME = user")
	dbase.commit()
	dbase.close()

def retrieveUser(userPhoneNumber):
	dbase = sqlite3.connect('Accounts.db')
	act = dbase.cursor()
	act.execute("SELECT ID, FIRSTNAME, LAST, USERNAME, PASSWORD, EMAIL, PHONENUMBER FROM AccountInfo WHERE PHONENUMBER = userPhoneNumber")
	dbase.commit()
	dbase.close()

def updatePhone(user, userPhoneNumber):
	dbase = sqlite3.connect('Accounts.db')
	act = dbase.cursor()
	act.execute("UPDATE AccountInfo SET PHONENUMBER = userPhoneNumber WHERE USERNAME = user")
	dbase.commit()
	dbase.close()

def updateName(user, userFirst, userLast):
	dbase = sqlite3.connect('Accounts.db')
	act = dbase.cursor()
	act.execute("UPDATE AccountInfo SET FIRSTNAME = userFirst, LAST = userLast WHERE USERNAME = user")
	dbase.commit()
	dbase.close()

def updateEmail(user, userEmail):
	dbase = sqlite3.connect('Accounts.db')
	act = dbase.cursor()
	act.execute("UPDATE AccountInfo SET EMAIL = userEmail WHERE USERNAME = user")
	dbase.commit()
	dbase.close()