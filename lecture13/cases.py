import sqlite3

con = sqlite3.connect("../firm.db")
sql = "SELECT number, client, amount FROM cases WHERE status = 'в работе'"
rows = con.execute(sql)

for amount, client, number in rows: 
    print(number, client, amount)

con.close() 