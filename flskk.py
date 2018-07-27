from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/weather')
def weather():
    z = [{'name': 'солнечная', 'imgs': 'static/sun.jpg'},
         {'name': 'пасмурная', 'imgs': 'static/cloud1.jpg'},
         {'name': 'дождливая', 'imgs': 'static/rain1.jpg'}]
    weather = random.choice(z)
    return render_template('wthr.html', wther=weather)


@app.route('/me')
def me():
    imag = 'static/me.jpg'
    return render_template('me.html', meimg='static/me.jpg')


app.run(debug=True, port=8080)
