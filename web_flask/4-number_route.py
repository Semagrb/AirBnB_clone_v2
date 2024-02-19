#!/usr/bin/python3
"""
This script starts a Flask web application.
"""

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define route for the root URL ('/')
@app.route('/', strict_slashes=False)
def index():
    """Returns a greeting message."""
    return 'Hello HBNB!'

# Define route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a string 'HBNB'."""
    return 'HBNB'

# Define route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Returns 'C ' followed by the value of the text variable."""
    return 'C ' + text.replace('_', ' ')

# Define route for '/python' and '/python/<text>'
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """Returns 'Python ' followed by the value of the text variable."""
    return 'Python ' + text.replace('_', ' ')

# Define route for '/number/<int:n>'
@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """Returns 'n is a number' only if n is an integer."""
    return "{} is a number".format(n)

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
