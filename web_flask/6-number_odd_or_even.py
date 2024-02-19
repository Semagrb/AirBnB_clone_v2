#!/usr/bin/python3
"""
This script starts a Flask web application.
"""

from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)


# Route for the root URL ('/')
@app.route('/', strict_slashes=False)
def index():
    """Returns a simple greeting."""
    return 'Hello HBNB!'


# Route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a string 'HBNB'."""
    return 'HBNB'


# Route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """
    Returns 'C ' followed by the value of the text variable.
    The underscores in the text are replaced with spaces.
    """
    return 'C ' + text.replace('_', ' ')


# Route for '/python' and '/python/<text>'
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """
    Returns 'Python ' followed by the value of the text variable.
    The underscores in the text are replaced with spaces.
    """
    return 'Python ' + text.replace('_', ' ')


# Route for '/number/<int:n>'
@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """
    Returns 'n is a number' only if n is an integer.
    """
    return "{:d} is a number".format(n)


# Route for '/number_template/<int:n>'
@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """
    Displays an HTML page only if n is an integer.
    The integer n is passed to the HTML template.
    """
    return render_template('5-number.html', n=n)


# Route for '/number_odd_or_even/<int:n>'
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersandevenness(n):
    """
    Displays an HTML page only if n is an integer.
    Determines if n is odd or even and passes this information
    along with n to the HTML template.
    """
    evenness = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           evenness=evenness)


# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

