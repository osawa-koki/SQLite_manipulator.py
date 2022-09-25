import sqlite3

dbname = "db/koko.sqlite"
connection = sqlite3.connect(dbname)
cursor = connection.cursor()

# SQL文の作成


connection.commit()
connection.close()


