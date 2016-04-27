from flask import Flask, render_template, request, url_for, redirect, session
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from functools import wraps

 
app = Flask(__name__)


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('homepage'))

    return wrap


@app.route('/', methods=["GET", "POST"])

def homepage():
    error = ''
    try:
        if request.method == "POST":
		
            attempted_username = request.form['username']
            attempted_password = request.form['password']

            #flash(attempted_username)
            #flash(attempted_password)

            if attempted_username == "Lister" and attempted_password == "1":
		session['logged_in'] = True
                return redirect(url_for('dashboard_page'))
				
            else:
                error = "Invalid credentials. Try Again."

        return render_template("index.html", error = error)

    except Exception as e:
        flash(e)
        return render_template("index.html", error = error) 


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@app.route('/dashboard/')
@login_required
def dashboard_page():
    return render_template("dashboard.html")


@app.route('/new')
@login_required
def nawpage():
    return render_template("new.html")


@app.route('/update')
@login_required
def updatePage():
    return render_template("index.html")


@app.route('/update/title')
@login_required
def updatetitlePage():
    return render_template("index.html")


@app.route('/update/price')
@login_required
def updatepricePage():
    return render_template("index.html")

@app.route('/update/description')
@login_required
def updatedescriptionPage():
    return render_template("index.html")


@app.route('/update/location')
@login_required
def updatelocationPage():
    return render_template("index.html")

if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)
