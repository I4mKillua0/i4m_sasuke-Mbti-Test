from flask import Flask, render_template, redirect, url_for, request, session
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    
    # Forward the request to the external URL
    url = 'https://www.16personalities.com/test-results'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
        'Accept': 'application/json, text/plain, */*',
    }
    
    response = requests.post(url, headers=headers, json=data)
    print(response.text)
    a=response.text.split('.com\\/')[1]
    b = a.split('-personality"}')[0]
    
    # Return the response from the external server back to the frontend
    return b




@app.route('/')
def index():
    return render_template('mbti.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
