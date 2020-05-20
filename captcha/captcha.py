
from flask import *
from os import urandom
from random import shuffle
from string import ascii_letters

CHAR_NUMBER = 5
app = Flask(__name__)

app.secret_key = urandom(15)

def generate():
    captcha = list(ascii_letters)
    shuffle(captcha)
    return ''.join(captcha[:CHAR_NUMBER])

@app.route('/')
def root():
    return redirect('http://localhost:5000/captcha') # não consegui usar o url_for

@app.route('/captcha', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        session['captcha'] = generate()
        return render_template('index.html', captcha = session['captcha'])

    elif request.method == 'POST':
        if request.form['answer'] == session['captcha']:
            return 'captcha certo'

        return 'captcha errado'

app.run()

