"""A Flask web application that implements a simple calculator.

This module provides a web interface for basic arithmetic operations including
addition, subtraction, multiplication, and division. The calculator handles
errors such as invalid input and division by zero. 0

Attributes:
    app: A Flask application instance.
    app.secret_key: A secret key required for form handling.

Routes:
    /: The main calculator page that handles both GET and POST requests.
"""

from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'calculator-secret-key'  # Required for form handling

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    error = None
    
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operator = request.form['operator']
            
            if operator == 'add':
                result = num1 + num2
            elif operator == 'subtract':
                result = num1 - num2
            elif operator == 'multiply':
                result = num1 * num2
            elif operator == 'divide':
                if num2 == 0:
                    error = "Error: Division by zero is not allowed"
                else:
                    result = num1 / num2
        except ValueError:
            error = "Error: Please enter valid numbers"
        except Exception as e:
            error = f"Error: {str(e)}"
    
    return render_template('calculator.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)