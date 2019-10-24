from flask import render_template, request, url_for, redirect
from flask import Flask
import sqlite3

# Устанавливаем соединение с БД
conn = sqlite3.connect("test.db", check_same_thread=False)

# Создаем курсор -- это специальный объект, который делает запросы и получает их результаты
cursor = conn.cursor()

app = Flask(__name__)

def getUser(login, password):
    u = "SELECT * FROM users WHERE login = '%s' and pass = '%s';" % (login, password)
    cursor.execute(u)
    result = cursor.fetchall()
    if len(result) == 1:
        return result[0]
    else:
        return "Error"       

def getQuestion(question):
    q = "SELECT * FROM questions WHERE question = '%s';" % (question)
    cursor.execute(u)
    result = cursor.fetchall()
    return result[0]    
       

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
            
            if user == "Error":
                error = "Неправильный логин или пароль"
            else: 
                return dashboard(user[1], user[2]) # Здесь: 1 - firstname, 2 - lastname
            print (url_for('dashboard'))
        return render_template("login.html", error = error)
            # return render_template("login.html", error = cursor.fetchall())
#            return redirect(url_for('dashboard') + "?name=%s&surname=%s" % (result[1], result[2]))
            
    
    #except Exception as e:
        
      #  return render_template("login.html", error = e)



if __name__ == '__main__':
	app.debug = True
	app.run()

# Закрываем соединение с БД    
conn.close()