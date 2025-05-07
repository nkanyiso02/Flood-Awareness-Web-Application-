from flask import Flask, render_template
from datetime import datetime
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flood_awareness.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/rural')
def rural():
    return render_template('rural.html')

@app.route('/urban')
def urban():
    return render_template('urban.html')

@app.route('/flood_prone_areas')
def flood_prone_areas():
    return render_template('flood_prone_areas.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/weather')
def weather():
    return render_template('weather.html')

if __name__ == "__main__":
    app.run(debug=True)
