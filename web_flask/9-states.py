#!/usr/bin/python3
"""
This script starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage

# Create a Flask application instance
app = Flask(__name__)


# Route for '/states' and '/states/<state_id>'
@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """
    Displays the states and cities listed in alphabetical order.
    If a state_id is provided, it includes the cities for that state.
    """
    # Retrieve all states from the storage
    states = storage.all("State")
    # If a state_id is provided, format it correctly
    if state_id is not None:
        state_id = 'State.' + state_id
    # Render the template '9-states.html' with the states data and state_id
    return render_template('9-states.html', states=states, state_id=state_id)


# Teardown function to close the storage connection
@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage connection on teardown."""
    storage.close()


# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
