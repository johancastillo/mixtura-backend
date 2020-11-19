# Import micro Framework Flask
from flask import Flask

# Intance of Flask class
app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return 'Hello world'

# About page
@app.route('/about')
def about():
    return 'It is page of about'

# Services page
@app.route('/services')
def services():
    return 'It is page of services'

# Run application
app.run()