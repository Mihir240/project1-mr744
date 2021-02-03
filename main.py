from flask import Flask, render_template
import os, random

app = Flask(__name__)

@app.route('/')
def main_app():

    return render_template(
        'index.html'
    )

app.run(
    port = int(os.getenv('PORT',8080)),
    host = os.getenv('IP','0.0.0.0'),
    debug = True
)