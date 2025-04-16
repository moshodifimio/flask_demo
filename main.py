# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import os

from flask import Flask

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/message')
def message():
    return os.getenv('MESSAGE')

@app.route('/number')
def number():
    return os.getenv('NUMBER')

# main driver function
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8000)), debug=True)
