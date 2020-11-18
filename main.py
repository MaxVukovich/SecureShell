#Luca Pinto
#Noobaka Irfan
#Tanmay Marwah
#Andrew Crisostomo
#Cody Peng
#Max Vukovich
#test
# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
import os
#yurrrrrr
#yolo
# create a Flask instance
app = Flask(__name__)

# connects default URL of server to a python function
@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html')

@app.route('/login', methods=['POST', 'GET'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('Wrong password!')
    return index()

@app.route('/links/')
def links_route():
    return render_template("links.html")

@app.route('/flask/')
def flask():
    return render_template("flask.html")

@app.route('/embedshell/')
def embed():
    return render_template("embedshell.html")

@app.route('/embedyoutube/')
def video():
    return render_template("embedyoutube.html")

@app.route('/project/journal1')
def journal1_route():
    return render_template("definedata.html", data=data.journal1())

@app.route('/project/journal2')
def journal2_route():
    return render_template("definedata.html", data=data.journal2())

@app.route('/backgroundbeat/')
def music():
    return render_template("backgroundbeat.mp3")

@app.route('/embedprojectplan/')
def embed1():
    return render_template("embedprojectplan.html")

@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'GET':
        return render_template("form.html")
    elif request.method == 'POST':
        if request.form.get('title') != '' and request.form.get('category') != ''  and request.form.get('description') != '' :
            title = request.form.get('title')
            category = request.form.get('category')
            description = request.form.get('description')
            return redirect("/showform?title=" + str(title) +"&category=" + str(category) + "&description=" + str(description), code=302)
        else:
            return render_template("form.html")

@app.route('/showform', methods=['POST', 'GET'])
def showform():
    title = request.args.get('title')
    category = request.args.get('category')
    description = request.args.get('description')
    return render_template("showform.html", title=title , description=description , category=category)


if __name__ == "__main__":
    # runs the application on the repl development server
    app.secret_key = os.urandom(12)
    app.run(debug=True)
