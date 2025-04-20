Usage Guide
===========

The Flask Calculator provides a simple web interface for performing basic arithmetic operations.

Basic Operations
--------------

The calculator supports four basic operations:

* Addition (+)
* Subtraction (-)
* Multiplication (×)
* Division (÷)

Using the Calculator
------------------

1. Enter the first number in the "First Number" field
2. Select the desired operation from the dropdown menu
3. Enter the second number in the "Second Number" field
4. Click the "Calculate" button to see the result

Example Usage
------------

Addition
~~~~~~~~

1. Enter ``5`` in the first number field
2. Select ``Addition (+)`` from the operation dropdown
3. Enter ``3`` in the second number field
4. Click "Calculate"
5. Result: ``8``

Division
~~~~~~~~

1. Enter ``15`` in the first number field
2. Select ``Division (÷)`` from the operation dropdown
3. Enter ``3`` in the second number field
4. Click "Calculate"
5. Result: ``5``

Error Handling
-------------

The calculator handles various error cases gracefully:

Division by Zero
~~~~~~~~~~~~~~~
If you attempt to divide by zero, the calculator will display an error message:
"Error: Division by zero is not allowed"

Invalid Input
~~~~~~~~~~~~
If you enter non-numeric values, the calculator will display:
"Error: Please enter valid numbers"