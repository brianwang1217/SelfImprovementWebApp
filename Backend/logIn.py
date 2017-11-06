#checks to see if the username and password match in datatable
#works, but still needs to be checked for exceptions
def logIn(user, userPassword):
	dbase = sqlite3.connect('Accounts.db')
	act = dbase.cursor()
	info = (user, userPassword)
	print(user, userPassword)
	if (act.execute("SELECT * FROM Accounts WHERE USERNAME = ? AND PASSWORD = ?", info).fetchone()[0]):
		information = (act.execute("SELECT * FROM Accounts WHERE USERNAME = ? AND PASSWORD = ?", info))
		for row in information:
			print (row[4]);
			if row[4] == userPassword:
				return True
	return False
