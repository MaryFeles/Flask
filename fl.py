from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/login')
@app.route('/login/<name>')
def login(name=None):
    return render_template('login.html', name=name)

if __name__ == '__main__':
	app.debug = True
	app.run()