import sqlite3

#Bunch of Database functions for reference, not all of them work lol

def insertAccount(ID, FIRSTNAME, LAST, USERNAME, PASSWORD, EMAIL, PHONENUMBER):
	dbase = sqlite3.connect("Accounts (2).db")
	act = dbase.cursor()
	act.execute("INSERT INTO Accountinfo (ID, FIRSTNAME, LAST, USERNAME, PASSWORD, EMAIL, PHONENUMBER) VALUES (?,?,?,?,?,?,?)", (9, "hello", "world", "this", "is", "tlk@gmail.com", "23532524"))
	act.commit()
	act.close()
	return "added"

insertAccount(9, "Shreyas", "Mohan", "shreyas", "cs196", "shreyas@gmail", "3453420")

'''
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
'''