from flask import render_template, request, url_for
from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html")

@app.route('/login/', methods=["GET","POST"])
def login_page():
    error = ''
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']
            
            if attempted_username == "admin" and attempted_password == "password":
                return redirect(url_for('dashboard'))
            else:
                error = "Try Again"
                
        return render_template("login.html", error = error)
    
    except Exception as e:
        
        return render_template("login.html", error = error)
            
if __name__ == '__main__':
	app.debug = True
	app.run()
