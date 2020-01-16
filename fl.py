from flask import render_template, request, url_for, redirect, session, escape
from flask import Flask
import sqlite3

# Устанавливаем соединение с БД
conn = sqlite3.connect("test.db", check_same_thread=False)

# Создаем курсор -- это специальный объект, который делает запросы и получает их результаты
cursor = conn.cursor()

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

def getUser(login, password):
    u = "SELECT * FROM users WHERE login = '%s' and pass = '%s';" % (login, password)
    cursor.execute(u)
    result = cursor.fetchall()
    if len(result) == 1:
        return result[0]
    else:
        return "Error"       

def getQuestions():
    q = "SELECT * FROM questions;"
    cursor.execute(q)
    return cursor.fetchall()

def getAnswers():
    #questions = getQuestions()
    #a = "SELECT answerText FROM answers WHERE questionID = '%s';" % (questions[0][0])
    a = "SELECT * FROM answers;"
    cursor.execute(a)
    return cursor.fetchall()
        
       

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/dashboard', methods=["GET","POST"])
def dashboard():
    if 'username' in session:
        questions = getQuestions()
        answers = getAnswers()
        login = session.get('username')
        password = session.get('password')
        user = getUser(login, password)
        name = user[1]
        surname = user[2]
        print (session['username'])
        if request.method == "POST":
            print (session)
           # ans = request.form['answer-list-1']
            print (ans)
        return render_template("dashboard.html", name = name, surname = surname, questions = questions, answers = answers)
    
#@app.route('/result', methods=["GET","POST"])
##def result(): 


@app.route('/login/', methods=["GET","POST"])
def login_page():
        error = ''
    #try:
        if request.method == "POST":
            session['username'] = request.form['username']
            session['password'] = request.form['password']
            attempted_username = request.form['username']
            attempted_password = request.form['password']
            user = getUser(attempted_username, attempted_password)
            
            if user == "Error":
                error = "Неправильный логин или пароль"
            else: 
                return redirect(url_for('dashboard'))

                #return dashboard(user[1], user[2]) # Здесь: 1 - firstname, 2 - lastname
            
        return render_template("login.html", error = error)
            # return render_template("login.html", error = cursor.fetchall())
            # return redirect(url_for('dashboard') + "?name=%s&surname=%s" % (result[1], result[2]))
            
    
    #except Exception as e:
        
      #  return render_template("login.html", error = e)

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('login_page'))

if __name__ == '__main__':
	app.debug = True
	app.run()

# Закрываем соединение с БД    
conn.close()
