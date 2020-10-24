
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    with open('mysite/new.sh', 'w') as f:
        f.write('#!/bin/bash')
        f.write('\n')
        f.write('echo hello')
        f.close()

    return 'Hello from Flask!'

