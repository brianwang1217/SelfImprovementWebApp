#!/usr/bin/python

import sqlite3

def insertAccount(first, last, user, userPassword, userEmail, userPhoneNumber):
	dbase = sqlite3.connect('Accounts.db')
	act = dbase.cursor()
	row = (first, last, user, userPassword, userEmail, userPhoneNumber)
	act.execute("INSERT INTO Accounts (FIRSTNAME, LASTNAME, USERNAME, PASSWORD, EMAIL, PHONENUMBER) VALUES (?, ?, ?, ?, ?, ?)", row)
	dbase.commit()
	dbase.close()

#insertAccount('Brian', 'Wang', 'brianwang', 'cs196', 'brian@gmail.com', 'asdf')


def retrieveUser(user):
 	dbase = sqlite3.connect('Accounts.db')
 	act = dbase.cursor()
 	str = user
 	act.execute("SELECT ID, FIRSTNAME, LASTNAME, USERNAME, PASSWORD, EMAIL, PHONENUMBER FROM Accounts WHERE USERNAME is (?, ? ,?,?,?,?,?,?,?)", user)
 	dbase.commit()
 	dbase.close()

print(retrieveUser('brianwang'))

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
