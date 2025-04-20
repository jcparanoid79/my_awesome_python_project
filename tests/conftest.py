import pytest
import sys
import os

# Add the src directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture(autouse=True)
def app_context():
    """Create a Flask application context for the tests."""
    from src.app import app

    with app.app_context():
        yield app
