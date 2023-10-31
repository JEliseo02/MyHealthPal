from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import requests

app = Flask(__name__)


#testing assignment
# Configuration
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Extensions initialization
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Routes
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        hashed_password = generate_password_hash(password, method='sha256')
        
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
    return render_template("register.html")
# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/food_list/', defaults={'goal': None}, methods=['GET'])
@app.route('/food_list/<goal>', methods=['GET'])
def food_list(goal):
    # Map user goals to Spoonacular diet options
    diet_map = {
        'bulking': 'Whole30',  # This is just a placeholder. You should choose an appropriate diet type from Spoonacular's options.
        'cutting': 'Ketogenic',
        'maintenance': 'Balanced'
    }

    if goal:
        diet = diet_map.get(goal)
        
        # Avoid exposing your API key directly in the code. Consider using environment variables.
        api_key = "a5e830b7c7764e80aab845f83c02feda"

        # Construct the API URL
        url = f"https://api.spoonacular.com/recipes/complexSearch?diet={diet}&apiKey={api_key}"
        
        response = requests.get(url)
        data = response.json()
        
        recipes = data.get('results', [])
    else:
        recipes = []

    return render_template('food_list.html', recipes=recipes, goal=goal)


@app.route('/calculations')
def calculations():
    return render_template('calculations.html')

@app.route('/exercise')
def exercise():
    return render_template('exercise.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check your login details and try again.', 'danger')
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/home")
@login_required
def home():
    return render_template("index.html")

# Helper functions
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

