import sqlite3

def insertFit(username, ex, message, day, hour, minute):
	dbase = sqlite3.connect("Notifications.db")
	act = dbase.cursor()

	row = (username, ex, message, day, hour, minute)
	act.execute("INSERT INTO Fitness (user, ex1, message1, day1, hour1, min1) VALUES (?,?,?,?,?,?)", row)
	dbase.commit()
	dbase.close()
	return True

def insertRem(username, rem, message, day, hour, minute):
	dbase = sqlite3.connect("Notifications.db")
	act = dbase.cursor()

	row = (username, rem, message, day, hour, minute)
	act.execute("INSERT INTO Reminders (user, rem1, message1, day1, hour1, min1) VALUES (?,?,?,?,?,?)", row)
	dbase.commit()
	dbase.close()
	return True

#given user, return all subject, message (Notifications.db), email (Accounts.db) [dictionary]
def returnAllReminders(username):
	dbase = sqlite3.connect("Notifications.db")
	act = dbase.cursor()
	row = act.execute("SELECT * FROM Reminders where user = ?", (format(username),))
	dic = {}
	for obj in row:
		dic[obj[1]] = obj[2]
	dbase.commit()
	dbase.close()
	return dic

#print(returnAllReminders("brian"))

def deleteRem(username, rem):
	dbase = sqlite3.connect("Notifications.db")
	act = dbase.cursor()
	info = (rem, username)
	act.execute("DELETE FROM Reminders WHERE rem1 = ? AND user = ?", info)
	dbase.commit()
	dbase.close()
	return True

def updateRem(username, rem, day, hour, minute):
	dbase = sqlite3.connect("Notifications.db")
	act = dbase.cursor()
	change = (day, hour, minute)
	row = (day, hour, minute, username, rem)
	act.execute("UPDATE Reminders SET day1 = ?, hour1 = ?, min1 = ? WHERE user = ? AND rem1 = ?", row)
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

def updateFit(username, rem, day, hour, minute):
	dbase = sqlite3.connect("Notifications.db")
	act = dbase.cursor()
	change = (day, hour, minute)
	row = (day, hour, minute, username, rem)
	act.execute("UPDATE Fitness SET day1 = ?, hour1 = ?, min1 = ? WHERE user = ? AND ex1 = ?", row)
	dbase.commit()
	dbase.close()
	return True

def getDayRem(username, rem):
	dbase = sqlite3.connect("Notifications.db")
	act = dbase.cursor()
	change = (username, rem)
	day = act.execute("SELECT * from Reminders where user = ? and rem1 = ?", change)
	for row in day:
		x = row[2]
	dbase.commit()
	dbase.close()
	return x

def getHourRem(username, rem):
	dbase = sqlite3.connect("Notifications.db")
	act = dbase.cursor()
	change = (username, rem)
	day = act.execute("SELECT * from Reminders where user = ? and rem1 = ?", change)
	for row in day:
		x = row[3]
	dbase.commit()
	dbase.close()
	return x

def getMinRem(username, rem):
	dbase = sqlite3.connect("Notifications.db")
	act = dbase.cursor()
	change = (username, rem)
	day = act.execute("SELECT * from Reminders where user = ? and rem1 = ?", change)
	for row in day:
		x = row[4]
	dbase.commit()
	dbase.close()
	return x

def getDayFit(username, rem):
	dbase = sqlite3.connect("Notifications.db")
	act = dbase.cursor()
	change = (username, rem)
	day = act.execute("SELECT * from Fitness where user = ? and rem1 = ?", change)
	for row in day:
		x = row[2]
	dbase.commit()
	dbase.close()
	return x

def getHourFit(username, rem):
	dbase = sqlite3.connect("Notifications.db")
	act = dbase.cursor()
	change = (username, rem)
	hour = act.execute("SELECT * from Fitness where user = ? and rem1 = ?", change)
	for row in hour:
		x = row[3]
	dbase.commit()
	dbase.close()
	return x

def getMinFit(username, rem):
	dbase = sqlite3.connect("Notifications.db")
	act = dbase.cursor()
	change = (username, rem)
	minute = act.execute("SELECT * from Fitness where user = ? and rem1 = ?", change)
	for row in minute:
		x = row[4]
	dbase.commit()
	dbase.close()
	return x

#print(getHourRem("brian", "pushups"))
