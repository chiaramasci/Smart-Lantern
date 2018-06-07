from flask import Flask, render_template,request,redirect
import database_functions as fn
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("database.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start")
def start():
    return render_template("start.html")

@app.route("/tutorial")
def tutorial():
    return render_template("tutorial.html")

@app.route("/getuserspositions")
def getuserspositions():
    pos = fn.get_users_positions()
    return render_template("positions.html", positions=pos)


@app.route("/nextdirection/<int:position_now>")
def next_direction(position_now):
    cursor  = conn.execute('SELECT * FROM PATH WHERE POSITION = %d' %position_now)
    next_dir = cursor.fetchall()[0][1]
    
    return str(next_dir)

@app.route("/createrecord/<ncard>/<username>/<int:position>/<direction>")
def createrecord(ncard,username,position,direction):
    fn.create_record(ncard,username,position,direction)
    return "record created successfully"

@app.route("/updaterecord/<ncard>/<int:position>/<direction>")
def updaterecord(ncard,position,direction):
    fn.update_record(ncard,position,direction)
    return "record updated successfully"

@app.route("/getdirectionraspberry/<ncard>")
def getdirectionraspberry(ncard):
    direction = fn.get_direction_raspberry(ncard)
    return direction

@app.route("/insertinitialdata", methods = ['POST','GET'])
def insertindata():
    if request.method == 'POST':
        ncard = request.form['ncard']
        username = request.form['username']
        print(ncard)
        fn.insert_initial_data(int(ncard),username)
        return redirect("/tutorial")
        #return redirect("/getinitialdata/"+ncard+"/"+username)
    else:
        return redirect("/tutorial.html")

@app.route("/insertinitialdata/<ncard>/<username>")
def insertinitialdata(ncard,username):
    fn.insert_initial_data(ncard,username)
    return "data inserted successfully"

@app.route("/getinitialdata/<ncard>")
def getinitialdata(ncard):
    #initial_data = fn.get_initial_data(ncard)
    cursor = conn.execute('SELECT * FROM START WHERE NCARD = %d' %(ncard))
    initial_data = cursor.fetchall()[0][1]
    return initial_data

@app.route("/getposition/<ncard>")
def getposition(ncard):
    cursor = conn.execute("SELECT ncard,username,position,direction FROM DATA WHERE NCARD = %d" %(ncard))
    #conn.close()
    pos = cursor.fetchall()[0][2]
    
    return str(pos)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
