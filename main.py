from flask import Flask
from app_views import HomePage, BillFormPage, ResultPage, BillForm

app = Flask(__name__)

# Register the class-based view with a URL
app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/result', view_func=ResultPage.as_view('result_page'))

if __name__ == "__main__":
    app.run(debug=True)
