from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/follow')
def follow_url():
    url = request.args.get('url', '')
    if url:
        # SSRF - Will CodeQL flag it in a new PR when it already exists as an alert?
        return requests.get(url).text

    return "No URL parameter provided."

@app.route('/')
def home():
    return '''<h1>SSRF</h1>
                <br>
                Usage: When the app is running, put in a desired URL to call from the app:
                    <br><code>http://127.0.0.1:5000/follow?url=https://api.github.com/events</code><br>
                <p></p>
                Running: Navigate to the directory containing ssrf.py and run:
                <br><code>
                    python3 ssrf.py
                </code></br>
    '''

if __name__ == '__main__':
    app.run(debug=True)
