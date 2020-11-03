#Luca Pinto
#Noobaka Irfan
#Tanmay Marwah
#Andrew Crisostomo
#Cody Peng
#Max Vukovich
#test
# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template , redirect, url_for, request

# create a Flask instance
app = Flask(__name__)

# connects default URL of server to a python function
@app.route('/')
def home():
    # function use Flask import (Jinga) to render an HTML template
    return render_template("home.html")

@app.route('/links/')
def links_route():
    return render_template("links.html")

@app.route('/flask/')
def flask():
    return render_template("flask.html")

@app.route('/embedshell/')
def embed():
    return render_template("embedshell.html")

@app.route('/login/', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True)
