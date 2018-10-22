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

    pwd_error = verify(v_pwd, password)
    username_error = ""
    email_error = ""

    
    if username == "":
        username_error = "Please choose a Username"
    else:
        username_error = check(username)
    
    if (pwd_error == "" and username_error == "" and email_error == ""):
        return redirect('/account')#add later

    template = jinja_env.get_template('create-account.html')
    return template.render(username=username, username_error=username_error, email=email, email_error=email_error, pwd_error=pwd_error)
    #incorrect form --redirect('/?username={0}&username_error={1}&email={2}&email_error={3}&pwd_error={4}'.format(username, username_error, email, email_error, pwd_error))

def verify(v_pwd, password):

    if v_pwd != password:
        return "Passwords do not match."
    if password == "":
        return "Please enter a password"
    else:
        return check(password)
    
def check(entry):
    if entry.length() < 3 or entry.length() > 20:
        return "Must be 3-20 characters."
    for a in entry:
        if a == " ":
            return "Must contain no spaces"
    return ""
    
def email_check(email):
    if check(email) != "":
        return check(email)
    else:
        for a in email:
            if a == "@":
                for b in range(email[a], email.length()-a-1, 1):
                    if a == ".":
                        return ""
    return "Please enter a valid email.(example@email.com)"

app.run()