from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    return render_template('login.html')

if __name__ == '__main__':
	app.debug = True
	app.run()
