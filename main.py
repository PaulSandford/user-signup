from flask import Flask, request, redirect
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja2_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir, autoescape = True))



@app.route("/")
def index():
    template = jinja_env.get_template('')#insert first template
    return template.render()


app.run()