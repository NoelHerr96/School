from flask import Flask, request, render_template, redirect, url_for, session
import random
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for session storage

# Serve the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "SikkerAdmin" and password == "password":
            # Set user session if login is successful
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return "Invalid username or password", 401  # Unauthorized

    return render_template('login.html')

# Serve the main page
@app.route('/verification')
def index():
    # Check if user is logged in
    if 'username' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))  # Redirect to login if not logged in


@app.route('/generate-OTP', methods=['GET', 'POST'])
def generate_OTP():
    OTP_gen = str(random.randint(1000, 9999))
    session['generated_OTP'] = OTP_gen
    session['OTP_verified'] = False  # Reset token verification status
    return f"Your generated 4-digit verification code is: {OTP_gen}"


# Route to verify the OTP
@app.route('/verify-OTP', methods=['POST'])
def verify_OTP():
    # Get individual digit inputs from the form
    entered_OTP = (
    request.form.get('code-1') +
    request.form.get('code-2') +
    request.form.get('code-3') +
    request.form.get('code-4')
    )
    
    generated_OTP = session.get('generated_OTP')

    if entered_OTP == generated_OTP:
        session['OTP_verified'] = True  # Set token as verified
        return redirect(url_for('flag'))
    else:
        return redirect(url_for('index'))
    
# Route for congratulations page
@app.route('/flag', methods=['GET'])
def flag():
    if session.get('OTP_verified'):
        return render_template('flag.html')
    else:
        return redirect(url_for('index'))  # Redirect if not verified

app.run(host='localhost', port=5000, debug=True)