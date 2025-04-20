# Simple Web Calculator

A web-based calculator application built with Flask that performs basic arithmetic calculations. The application provides a clean, user-friendly interface for performing simple mathematical operations through your web browser.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Clean and intuitive web interface
- Error handling for invalid inputs and division by zero
- Responsive design for various screen sizes

## Prerequisites

- Python 3.8 or higher
- UV package manager (recommended for dependency management)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd my_awesome_python_project
```

2. Create and activate a virtual environment using UV:
```bash
uv venv .venv
# On Windows:
.venv\Scripts\activate
# On Unix or MacOS:
source .venv/bin/activate
```

3. Install dependencies:
```bash
uv pip install -r requirements.txt
```

## Running the Application

1. Make sure you're in the project root directory
2. Run the Flask application:
```bash
python src/app.py
```
3. Open your web browser and navigate to `http://localhost:5000`

## Running Tests

The project includes a comprehensive test suite. To run the tests:

```bash
uv run pytest
```

## Usage Examples

1. Basic Addition:
   - Enter first number: 5
   - Enter second number: 3
   - Select operation: Add
   - Result: 8

2. Division:
   - Enter first number: 15
   - Enter second number: 3
   - Select operation: Divide
   - Result: 5

## Error Handling

The calculator handles various error cases:
- Division by zero
- Invalid numeric inputs
- Missing input fields

## Project Structure

```
├── src/
│   ├── app.py                 # Main application file
│   ├── requirements.txt       # Project dependencies
│   └── templates/
│       └── calculator.html    # HTML template for the calculator
├── tests/
│   ├── conftest.py           # Test configurations and fixtures
│   └── test_calculator.py    # Test cases for calculator functionality
└── requirements.txt          # Project dependencies
```

## Future Enhancements

- Advanced mathematical operations (exponents, square root)
- Calculation history
- Enhanced UI with CSS
- Client-side input validation
- More complex error handling