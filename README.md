# iPortfolio Django

iPortfolio Django is a Django web application where a user can showcase their personal information, skills, education and experience, portfolio projects, and services. Users can also send emails directly through the site.

## Installation

Follow the steps below to install and run the project on your local machine.

### Prerequisites

You will need the latest version of Python to run the project. You can download Python from the [official website](https://www.python.org/).

### Installation

1. Clone this repo to your local machine.
2. Create and activate a virtual environment in the directory where the project is located.
3. Run the command `pip install -r requirements.txt` to install the dependencies listed in the `requirements.txt` file.
4. Adjust your email settings in the `settings.py` file.
5. Adjust the email sending functions in the `views.py` file.
6. Run the command `python manage.py migrate` to create the database.
7. Start the server with the command `python manage.py runserver`.

## Usage

After running the web application on the local server, you can use the application by typing `http://127.0.0.1:8000/` into the address bar of your browser.
