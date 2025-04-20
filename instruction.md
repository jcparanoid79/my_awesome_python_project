# Instruction: Build a Web Calculator with Flask

## Task Goal

Create a simple web application using the Flask framework that functions as a basic arithmetic calculator. The application should present a form to the user in a web browser, allow them to input two numbers and select an operation (addition, subtraction, multiplication, or division), and then display the result on the same or a different page.

## Required Components

1.  **`app.py`:** The main Python file for the Flask application. This will handle routing, form processing, calculation logic, and rendering templates.
2.  **`templates/` directory:** A folder to store HTML template files.
3.  **`templates/calculator.html`:** An HTML file containing the form for user input (two number fields, an operator selection, and a submit button) and a place to display the result.

## Dependencies

* `Flask`: The web framework.

## Implementation Steps

1.  **Set up the Flask Application:**
    * Import the necessary components from `flask` (`Flask`, `render_template`, `request`).
    * Create a Flask application instance.
    * Define a secret key (good practice for forms, though not strictly necessary for this basic example's functionality).
2.  **Create the HTML Template (`calculator.html`):**
    * Create a standard HTML5 structure.
    * Include a `<form>` element that submits data to a specific URL (e.g., `/calculate`) using the `POST` method.
    * Inside the form, add two `<input type="number">` fields for the numbers (give them `name` attributes like `num1` and `num2`).
    * Add a `<select>` element for the operator, with `<option>` values like `add`, `subtract`, `multiply`, `divide` (give it a `name` attribute like `operator`).
    * Add a `<button type="submit">` for submitting the form.
    * Include a placeholder (e.g., a `<div>` or `<p>`) where the calculation result will be displayed. Use Jinja2 templating syntax (e.g., `{{ result }}`) to conditionally display the result if available.
3.  **Define Flask Routes:**
    * Create a route for the main calculator page (e.g., `/` or `/calculator`). This route should handle both `GET` and `POST` requests.
    * For `GET` requests to this route:
        * Render the `calculator.html` template. Pass no result initially.
    * For `POST` requests to this route (when the form is submitted):
        * Retrieve the values for `num1`, `num2`, and `operator` from `request.form`.
        * **Implement Calculation Logic:**
            * Convert `num1` and `num2` from strings (received from `request.form`) to numbers (e.g., floats or integers). Include basic error handling (e.g., using a `try-except` block) in case the conversion fails.
            * Use conditional logic (if/elif/else) based on the `operator` value to perform the correct arithmetic operation.
            * Handle the division-by-zero case gracefully (e.g., return an error message).
        * Store the result or error message in a variable.
        * Render the `calculator.html` template again, passing the calculated `result` (or error message) to the template so it can be displayed.
4.  **Run the Flask Application:**
    * Add the standard `if __name__ == '__main__':` block to run the Flask development server.

## Specific Logic Details

* The application should support addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
* Input numbers should be treated as floating-point numbers to handle decimals.
* Division by zero should result in a specific error message displayed to the user, rather than crashing the application.
* The result should be displayed clearly on the web page after a calculation is performed.

## Project Structure


my_calculator_project/
├── .gitignore
├── requirements.txt
├── app.py
└── templates/
└── calculator.html


## Next Steps (after implementing this instruction)

* Add more robust input validation.
* Improve the user interface styling (CSS).
* Add more advanced calculator features (e.g., more operations, history).
* Write tests for the calculation logic.
