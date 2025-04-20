Installation
============

This guide will help you set up the Flask Calculator application on your system.

Prerequisites
------------

* Python 3.8 or higher
* UV package manager (recommended)

Step-by-Step Installation
------------------------

1. Clone the Repository
~~~~~~~~~~~~~~~~~~~~~~

First, clone the repository to your local machine::

    git clone <repository-url>
    cd my_awesome_python_project

2. Create Virtual Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create and activate a virtual environment using UV::

    uv venv .venv
    
    # On Windows:
    .venv\Scripts\activate
    
    # On Unix or MacOS:
    source .venv/bin/activate

3. Install Dependencies
~~~~~~~~~~~~~~~~~~~~~

Install the required packages using UV::

    uv pip install -r requirements.txt

Verification
-----------

To verify that the installation was successful, run the application::

    python src/app.py

Then open your web browser and navigate to ``http://localhost:5000``. You should see the calculator interface.