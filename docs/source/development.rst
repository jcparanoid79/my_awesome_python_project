Development Guide
=================

This guide covers development practices, testing, and contributing to the Flask Calculator project.

Project Structure
----------------

.. code-block:: none

    my_awesome_python_project/
    ├── src/
    │   ├── app.py                 # Main application file
    │   ├── requirements.txt       # Project dependencies
    │   └── templates/
    │       └── calculator.html    # HTML template
    ├── tests/
    │   ├── conftest.py           # Test configurations
    │   └── test_calculator.py    # Test cases
    └── docs/                      # Documentation

Testing
-------

The project uses pytest for testing. To run the tests::

    pytest

Test Coverage::

    pytest --cov=src tests/

Available Test Cases
~~~~~~~~~~~~~~~~~~~

* test_homepage_get: Verifies the homepage loads correctly
* test_addition: Tests addition operation
* test_subtraction: Tests subtraction operation
* test_multiplication: Tests multiplication operation
* test_division: Tests division operation
* test_division_by_zero: Tests division by zero error handling
* test_invalid_input: Tests invalid input error handling

Contributing
-----------

1. Fork the repository
2. Create a feature branch
3. Write tests for new features
4. Implement your changes
5. Run the test suite
6. Submit a pull request

Code Style
---------

This project follows PEP 8 style guidelines. Use tools like ruff for linting::

    ruff check .

Documentation
------------

The project uses Sphinx for documentation. To build the docs::

    cd docs
    make html

The documentation will be available in ``docs/build/html/``