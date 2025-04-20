API Reference
=============

This section provides detailed documentation for the Flask Calculator's API.

Web Application
--------------

.. automodule:: app
   :members:
   :undoc-members:
   :show-inheritance:

Routes
------

Calculator Endpoint
~~~~~~~~~~~~~~~~~

The main calculator endpoint handles both GET and POST requests.

GET /
^^^^^
Displays the calculator interface.

**Response**: HTML page with the calculator form

POST /
^^^^^^
Processes calculation requests.

**Request Parameters**:

* ``num1`` (float): First number
* ``num2`` (float): Second number
* ``operator`` (string): Operation to perform (add, subtract, multiply, divide)

**Response**: HTML page with the calculation result or error message

Example successful response:

.. code-block:: html

    <div class="result success">
        Result: 8.00
    </div>

Error Handling
-------------

The API handles the following error cases:

* ValueError: When non-numeric values are provided
* ZeroDivisionError: When attempting to divide by zero
* General exceptions: Any other unexpected errors

Templates
--------

calculator.html
~~~~~~~~~~~~~~

The main template that provides the calculator interface. It includes:

* Input fields for two numbers
* Operation selection dropdown
* Calculate button
* Result/error display area