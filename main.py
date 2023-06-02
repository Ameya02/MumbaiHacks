from flask import Flask, render_template,url_for
from lorem_text import lorem
app = Flask(__name__,template_folder='template')


@app.route("/")
def index():
    lorem_text = lorem.paragraph()
    return render_template('index.html', text=lorem_text)

@app.route("/result")
def result():
    return render_template("result.html")