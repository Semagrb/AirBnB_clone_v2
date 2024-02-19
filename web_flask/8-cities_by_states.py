#!/usr/bin/python3
"""
This script starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage

# Create a Flask application instance
app = Flask(__name__)


# Route for '/cities_by_states'
@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Displays the states and cities listed in alphabetical order.
    Retrieves states and cities data from the storage.
    """
    # Retrieve all states from the storage
    states = storage.all("State").values()
    # Render the template '8-cities_by_states.html' with the states data
    return render_template('8-cities_by_states.html', states=states)


# Teardown function to close the storage connection
@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage connection on teardown."""
    storage.close()


# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
