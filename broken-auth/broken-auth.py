from flask import Flask, render_template, request, redirect, session, url_for
import datetime

app = Flask(__name__, template_folder='templates')
app.secret_key = b'secret_key'

# Simulated user data
users = {
    'user1': {'password': 'password1'},
    'user2': {'password': 'password2'},
}

# Simulated active sessions
active_sessions = {}

# Add a route for the root URL
@app.route('/')
def index():
    return render_template('index.html')

# Route to simulate login
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and users[username]['password'] == password:
        session['username'] = username
        active_sessions[username] = datetime.datetime.now()
        return redirect(url_for('dashboard'))

    return 'Invalid username or password'

# Route to simulate the dashboard
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        active_sessions[username] = datetime.datetime.now()
        return f'Welcome, {username}! This is your dashboard.'

    return redirect(url_for('login'))

# Route to simulate automatic logout after 5 seconds of inactivity
@app.before_request
def check_session_timeout():
    if 'username' in session:
        username = session['username']
        last_active_time = active_sessions.get(username, datetime.datetime.now())
        current_time = datetime.datetime.now()

        if (current_time - last_active_time).days > 5000:
            del session['username']
            return redirect(url_for('login'))

# Route to simulate logout
@app.route('/logout')
def logout():
    if 'username' in session:
        del session['username']
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
