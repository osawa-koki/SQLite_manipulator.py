import sqlite3

dbname = "db/koko.sqlite"
connection = sqlite3.connect(dbname)
cursor = connection.cursor()

# SQL文の作成

cursor.execute("SELECT number FROM pokemon WHERE number = ?;", (152, ))

if cursor.fetchone() == None:
	print(1)

print(2)

connection.commit()
connection.close()


