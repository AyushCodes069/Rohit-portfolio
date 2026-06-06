import os
import json
import time
import threading
import urllib.request
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/achievements')
def achievements():
    return render_template('achievements.html')

if __name__ == '__main__':
    app.run(debug=True)