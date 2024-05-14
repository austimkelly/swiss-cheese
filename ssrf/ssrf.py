from flask import Flask, request
import requests

app = Flask(__name__)

def fetch_url_content():
    url = request.args.get('url', '')
    if url:
        # New vulns introduced at a new line
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to fetch URL: {response.status_code}"
    else:
        return "No URL parameter provided."

@app.route('/follow')
def follow_url():
    url = request.args.get('url', '')
    if url:
        # SSRF - This will not be blocked in the PR because it already exists as an alert.
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
