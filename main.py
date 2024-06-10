import os
from flask import Flask
from dotenv import load_dotenv
from app_views import HomePage, BillFormPage, BillForm, ResultPage

# Load environment variables from a .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Set the secret key from the environment variable for session management and flashing messages
app.secret_key = os.getenv('APP_SECRET_KEY')  # Required for flashing messages

# Register the class-based views with their corresponding URLs
app.add_url_rule('/', view_func=HomePage.as_view('home_page')
                 )  # Home page route
# Bill form route
app.add_url_rule(
    '/bill_form', view_func=BillFormPage.as_view('bill_form_page'))
# Result page route
app.add_url_rule('/result', view_func=ResultPage.as_view('result_page'))

if __name__ == "__main__":
    # Run the Flask application in debug mode
    app.run(debug=True)
