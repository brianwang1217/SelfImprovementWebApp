import sqlite3

def insertFit(username, ex, day, hour, minute):
	dbase = sqlite3.connect("Notifications.db")
	act = dbase.cursor()

	row = (ex, day, hour, minute, username)
	act.execute("INSERT INTO Fitness (ex1, day1, hour1, min1, user) VALUES (?,?,?,?,?)", row)
	dbase.commit()
	dbase.close()
	return True

def insertRem(username, rem, day, hour, minute):
	dbase = sqlite3.connect("Notifications.db")
	act = dbase.cursor()

	row = (username, rem, day, hour, minute)
	act.execute("INSERT INTO Reminders (user, rem1, day1, hour1, min1) VALUES (?,?,?,?,?)", row)
	dbase.commit()
	dbase.close()
	return True

def deleteRem(username, rem):
	dbase = sqlite3.connect("Notifications.db")
	act = dbase.cursor()
	info = (rem, username)
	act.execute("DELETE FROM Reminders WHERE rem1 = ? AND user = ?", info)
	dbase.commit()
	dbase.close()
	return True

def deleteFit(username, ex):
	dbase = sqlite3.connect("Notifications.db")
	act = dbase.cursor()
	info = (ex, username)
	act.execute("DELETE FROM Fitness WHERE ex1 = ? AND user = ?", info)
	dbase.commit()
	dbase.close()
	return True
