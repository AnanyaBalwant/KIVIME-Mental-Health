from flask import Flask, json, redirect, render_template, flash, request, url_for, after_this_request, jsonify, send_from_directory
from flask.globals import request, session
from flask.helpers import url_for
from flask_login import UserMixin, LoginManager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_required,logout_user,login_user,login_manager,LoginManager,current_user
import json
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
import os
import secrets
from chatbot import get_mental_health_response
from datetime import datetime

# Initialize a simple model instead of loading from pickle
model = RandomForestClassifier(n_estimators=100, random_state=42)
# Train the model with some default values (this is just for testing)
X_dummy = np.random.rand(100, 4)  # 4 features: sleep, bp, respiration, heart rate
y_dummy = np.random.randint(0, 2, 100)  # Binary classification: 0=Normal, 1=Stress
model.fit(X_dummy, y_dummy)

# Create users.json if it doesn't exist
if not os.path.exists('users.json'):
    with open('users.json', 'w') as f:
        json.dump({}, f)

# Create journals directory if it doesn't exist
if not os.path.exists('journals'):
    os.makedirs('journals')

class User(UserMixin):
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

    @staticmethod
    def get(user_id):
        with open('users.json', 'r') as f:
            users = json.load(f)
            for username, data in users.items():
                if str(data['id']) == str(user_id):
                    return User(user_id, username)
        return None

#creation of the Flask Application named as "app"
# mydatabase connection
local_server=True
app=Flask(__name__)


app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

# Generate a secure random secret key
secret_key = secrets.token_hex(32)  # 32 bytes of random data
app.config['SECRET_KEY'] = secret_key
app.secret_key = secret_key

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def home():
    return render_template('index.html')

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        username = request.form.get('usn')
        password = request.form.get('pas')
        
        with open('users.json', 'r') as f:
            users = json.load(f)
        
        if username in users:
            flash("UserID is already taken", "warning")
            return redirect(url_for('signup'))
        
        # Generate new user ID
        user_id = len(users) + 1
        
        # Hash password and store user
        hashed_password = generate_password_hash(password)
        users[username] = {
            'id': user_id,
            'password': hashed_password
        }
        
        with open('users.json', 'w') as f:
            json.dump(users, f, indent=4)
        
        flash("SignUp Success Please Login", "success")
        return redirect(url_for('login'))
    
    return render_template("usersignup.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        username = request.form.get('usn')
        password = request.form.get('pas')
        
        with open('users.json', 'r') as f:
            users = json.load(f)
        
        if username in users and check_password_hash(users[username]['password'], password):
            user = User(users[username]['id'], username)
            login_user(user)
            flash("Login Success", "info")
            return redirect(url_for('home'))
        else:
            flash("Invalid Credentials", "danger")
            return redirect(url_for('login'))
    
    return render_template("userlogin.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout Successful", "warning")
    return redirect(url_for('login'))


@app.route('/music')
@login_required
def music():
    return render_template('music.html')


@app.route('/quizandgame')
@login_required
def quizandgame():
    return render_template('quizandgame.html')

    
@app.route('/exercises')
@login_required
def exercises():
    return render_template('exercises.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/game')
def game():
    return render_template('game.html')


@app.route('/i')
def i():
    return render_template('stress.html')



@app.route('/stressdetect', methods=['POST'])
def stressdetect():
    try:
        # Get form values
        sleep_hours = float(request.form.get('rr'))  # sleep hours
        blood_pressure = float(request.form.get('bp'))  # blood pressure
        respiration_rate = float(request.form.get('bo'))  # respiration rate
        heart_rate = float(request.form.get('hr'))  # heart rate
        
        # Create feature array
        features = np.array([[sleep_hours, blood_pressure, respiration_rate, heart_rate]])
        
        # Make prediction
        prediction = model.predict(features)[0]
        
        # Determine message based on prediction
        if prediction == 0:
            data = "You are having Normal Stress Level. Keep taking care of yourself!"
        else:
            data = "You are having High Stress Level! Consider consulting a doctor and get support from our chatbot."
        
        return render_template('stress.html', prediction_text3='Stress Level Result: {}'.format(data))
    
    except Exception as e:
        return render_template('stress.html', prediction_text3='Error: Please enter valid numerical values within the specified ranges.')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'No message provided'}), 400
            
        user_message = data['message'].strip()
        if not user_message:
            return jsonify({'error': 'Empty message'}), 400
            
        # Get response from Gemini
        response = get_mental_health_response(user_message)
        
        if response:
            return jsonify({'response': response})
        else:
            return jsonify({'error': 'Could not generate response'}), 500
            
    except Exception as e:
        print(f"Error in chat route: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/journal')
@login_required
def journal():
    # Debug logging
    print(f"Accessing journal route - User: {current_user.id}")
    # Get user's journal entries
    journal_file = f'journals/{current_user.id}_journal.json'
    entries = []
    if os.path.exists(journal_file):
        with open(journal_file, 'r') as f:
            entries = json.load(f)
    print(f"Found {len(entries)} entries for user {current_user.id}")
    return render_template('journal.html', entries=entries)

@app.route('/add_entry', methods=['POST'])
@login_required
def add_entry():
    title = request.form.get('title', '')
    content = request.form.get('content', '')
    mood = request.form.get('mood', '')
    
    if not title or not content:
        flash('Title and content are required!', 'error')
        return redirect(url_for('journal'))
    
    # Create new entry
    entry = {
        'id': datetime.now().strftime('%Y%m%d%H%M%S'),
        'title': title,
        'content': content,
        'mood': mood,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # Save to user's journal file
    journal_file = f'journals/{current_user.id}_journal.json'
    entries = []
    if os.path.exists(journal_file):
        with open(journal_file, 'r') as f:
            entries = json.load(f)
    
    entries.insert(0, entry)  # Add new entry at the beginning
    
    with open(journal_file, 'w') as f:
        json.dump(entries, f, indent=4)
    
    flash('Journal entry added successfully!', 'success')
    return redirect(url_for('journal'))

@app.route('/delete_entry/<entry_id>')
@login_required
def delete_entry(entry_id):
    journal_file = f'journals/{current_user.id}_journal.json'
    if os.path.exists(journal_file):
        with open(journal_file, 'r') as f:
            entries = json.load(f)
        
        entries = [e for e in entries if e['id'] != entry_id]
        
        with open(journal_file, 'w') as f:
            json.dump(entries, f, indent=4)
        
        flash('Entry deleted successfully!', 'success')
    return redirect(url_for('journal'))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path),
                             'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)