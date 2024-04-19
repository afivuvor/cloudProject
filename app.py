# from flask import Flask, render_template, request, redirect, url_for
from flask import *
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
load_dotenv()

app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')

app.secret_key = os.urandom(24)

# Database Connection
client = MongoClient('mongodb+srv://yasmin:VSTvDkc5dMvMXLGq@cluster0.ql0azoa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['ecommerce-db'] 
users_collection = db['users']  # Assuming you have a collection named 'users

session = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/sign_in')
def sign_in():
    
    return render_template('users/sign_in.html')

@app.route('/users/sign_up')
def sign_up():
    return render_template('users/sign_up.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # Retrieve the username and password from the form
        email = request.form['email']
        password = request.form['password']
        
        # Check if the user exists in the database
        user = users_collection.find_one({'email': email, 'password': password})        
        
        if user:
            print(user['email'])
            session['email'] = email
            session['name'] = user['name']
            return redirect(url_for('index'))
        else:
            return redirect(url_for('sign_in'))

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sell_now')
def sell_now():
    return render_template('sellnow.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/shopping_cart')
def shopping_cart():
    return render_template('shopping_cart.html')

# @app.teardown_appcontext
# def close_connection(exception):
#     client.close()

if __name__ == '__main__':
    app.run()
