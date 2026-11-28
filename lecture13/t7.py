import sqlite3

con = sqlite3.connect("../firm.db")
sql = "Select amount, client, number from cases where status = 'выиграно'"
rows = con.execute(sql)

count = 0
for row in rows:
    print(row[0])
    count = count + 1
print("Количество выигранных дел:", count)