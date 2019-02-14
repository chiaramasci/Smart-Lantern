import sqlite3

conn = sqlite3.connect("database.db")
print("connection successfull to table PATH")

print("ACTION?")
print("1 reset path")
print("2 insert new values for every position")
print("3 insert new value for a specific position")

action = int(input())

if(action == 1):
    for i in range(0,3):
        conn.execute("INSERT INTO PATH (position,direction) VALUES(%d,'unknown')" %i)
        conn.commit()
if(action == 2):
    for i in range(0,3):
        print("value for %d:" %i)
        nextd = input()
        conn.execute("UPDATE PATH SET DIRECTION = '%s' WHERE POSITION = %d" %(nextd,i))
        conn.commit()
if(action == 3):
    print("position to be modified: ")
    pos = int(input())
    print("direction to be inserted: ")
    dire = input()
    conn.execute("UPDATE PATH SET DIRECTION = '%s' WHERE POSITION = %d" %(dire,pos))
    comm.commit()

print("content")
cursor = conn.execute("SELECT * FROM PATH")
rows = cursor.fetchall()

for i in range(0,len(rows)):
    print(rows[i])

conn.close()
