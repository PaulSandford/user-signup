from flask import Flask, request, redirect
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir, autoescape = True))



@app.route("/")
def index():
    template = jinja_env.get_template('create-account')
    return template.render()

@app.route("/create", methods=['POST'])
def create():
    username = request.form['username']
    password = request.form['password']
    v_pwd = request.form['verify_password']
    email = request.form['email']

    pwd_error = ""
    username_error = ""
    email_error = ""

    if v_pwd != password:
        pwd_error = "Passwords do not match."
    if password == "":
        pwd_error = "Please enter a password"
    if username == "":
        username_error = "Please choose a Username"
    if (pwd_error == "" and username_error == "" and email_error == ""):
        return redirect('/account')#add later

    return redirect('/?username={0}&username_error={1}&email={2}&email_error={3}&pwd_error={4}'.format(username, username_error, email, email_error, pwd_error))

def verify(v_pwd, password):
    return True


app.run()