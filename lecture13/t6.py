import sqlite3

con = sqlite3.connect("../firm.db")
sql = "Select number from cases where client = 'ТОО Альфа'"
rows = con.execute(sql)

for row in rows:
    print("номера дел:", row[0])