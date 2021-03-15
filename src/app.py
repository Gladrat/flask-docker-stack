from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html.jinja')

@app.errorhandler(404)
def page_not_found(error):
    return 'ToDo: 404 template', 404