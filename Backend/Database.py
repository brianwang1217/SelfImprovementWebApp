import sqlite3

def insertAccount(ID, FIRSTNAME, LAST, USERNAME, PASSWORD, EMAIL, PHONENUMBER):
	dbase = sqlite3.connect("Accounts (2).db")
	act = dbase.cursor()
	act.execute("INSERT INTO Accountinfo (ID, FIRSTNAME, LAST, USERNAME, PASSWORD, EMAIL, PHONENUMBER) VALUES (?,?,?,?,?,?,?)", (9, "hello", "world", "this", "is", "tlk@gmail.com", "23532524"))
	act.commit()
	act.close()
	return "added"

insertAccount(9, "Shreyas", "Mohan", "shreyas", "cs196", "shreyas@gmail", "3453420")

def retrieveUser(user):
 	dbase = sqlite3.connect('Accounts.db') 
 	act = dbase.cursor()
 	str = (user)
 	row = act.execute("SELECT ID, FIRSTNAME, LASTNAME, USERNAME, PASSWORD, EMAIL, PHONENUMBER FROM Accounts WHERE USERNAME = ?", (format(user),))
 	return row
 	dbase.commit()
 	dbase.close()


def retrieveUser(userPhoneNumber):
	dbase = sqlite3.connect('Accounts.db')
	act = dbase.cursor()
	row = act.execute("SELECT ID, FIRSTNAME, LASTNAME, USERNAME, PASSWORD, EMAIL, PHONENUMBER FROM Accounts WHERE PHONENUMBER = ?", (format(userPhoneNumber),))
	#print
	'''
	for info in row:
		for i in range(0, len(info)):
			print(info[i])
	'''
	return row
	dbase.commit()
	dbase.close()
	
#print(retrieveUser('911'))

def updatePhone(user, userPhoneNumber):
	dbase = sqlite3.connect('Accounts.db')
	act = dbase.cursor()
	info = (userPhoneNumber, user)
	act.execute("UPDATE Accounts SET PHONENUMBER = ? WHERE USERNAME = ?", info)
	dbase.commit()
	dbase.close()

def updateName(user, userFirst, userLast):
	dbase = sqlite3.connect('Accounts.db')
	act = dbase.cursor()
	act.execute("UPDATE Accounts SET FIRSTNAME = userFirst, LASTNAME = userLast WHERE USERNAME = ?", (format(user),))
	dbase.commit()
	dbase.close()

def updateEmail(user, userEmail):
	dbase = sqlite3.connect('Accounts.db')
	act = dbase.cursor()
	act.execute("UPDATE Accounts SET EMAIL = userEmail WHERE USERNAME = ?", (format(user),))
	dbase.commit()
	dbase.close()
