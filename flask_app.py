
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import random, os

app = Flask(__name__)


@app.route('/')
def hello_world():
    with open('/home/rayan13/mysite/new.txt', 'w') as f:
        x = ''
        alphs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v']

        for i in range(20):
            x = x + random.choice(alphs)

        f.write(x)
    os.chdir('/home/rayan13/mysite/')
    os.system('git add new.txt')
    os.system('git commit -m "new update"')
    os.system('git push')
    return f'<h1>Hello from Flask! {x}</h1><a href="/">Reload</a>'
