import os
from flask import Flask
from dotenv import load_dotenv
from app_views import IndexView, BillFormView

# Load environment variables from a .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Set the secret key from the environment variable for session management and flashing messages
app.secret_key = os.getenv('APP_SECRET_KEY')  # Required for flashing messages


# Register the class-based views with their corresponding URLs
app.add_url_rule('/', view_func=IndexView.as_view('index_view')
                 )  # Home page route
# Bill form route
app.add_url_rule(
    '/bill_form', view_func=BillFormView.as_view('bill_form_view'), methods=['GET', 'POST'])


if __name__ == "__main__":
    # Run the Flask application in debug mode
    app.run(debug=True)
