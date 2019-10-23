from flask import render_template, request, url_for, redirect
from flask import Flask
import sqlite3

conn = sqlite3.connect("test.db", check_same_thread=False)
cursor = conn.cursor()

app = Flask(__name__)

def getUser(login, password):
    a = "select * from users where login = '%s' and pass = '%s';" % (login, password)
    cursor.execute(a)
    result = cursor.fetchall()
    if len(result) == 1:
        return result[0]
    else:
        return "Try again"             
       

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/dashboard')
def dashboard(name, surname):
#    a = request.args
#    name = a.to_dict()['name']
#    surname = a.to_dict()['surname']
    return render_template("dashboard.html", name = name, surname = surname)
    


@app.route('/login/', methods=["GET","POST"])
def login_page():
        error = ''
    #try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']
            
            user = getUser(attempted_username, attempted_password)
            
            if user == "Try again":
                error = "Try again"
            else: 
                return dashboard(user[1], user[2])
            print (url_for('dashboard'))
        return render_template("login.html", error = error)
            # return render_template("login.html", error = cursor.fetchall())
#            return redirect(url_for('dashboard') + "?name=%s&surname=%s" % (result[1], result[2]))
            
    
    #except Exception as e:
        
      #  return render_template("login.html", error = e)
            
if __name__ == '__main__':
	app.debug = True
	app.run()
