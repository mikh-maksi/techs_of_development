
import sqlite3
import datetime
    
conn = sqlite3.connect('example.db')
cur = conn.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS finances(
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    sum INTEGER,
#    cat VARCHAR(20),
#    sumdate TIMESTAMP);
# """)
# sql = f"INSERT INTO finances(sum, cat, sumdate) VALUES(30, 'transport','{datetime.datetime.now()}');"
sql = f"SELECT * FROM finances WHERE sumdate >= '2021-11-29 12:16:32.890659';"

print(sql)
cur.execute(sql)

results = cur.fetchall()
print(results)

sum = 0
for res in results:
    print(res[1])
    sum = sum + res[1]

print(sum)
conn.commit()
