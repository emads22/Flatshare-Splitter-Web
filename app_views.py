from flask import render_template
from flask.views import MethodView
from wtforms import Form

class HomePage(MethodView):
    def get(self):
        return render_template('index.html')

    def post(self):
        pass


class BillFormPage(MethodView):
    def get(self):
        return render_template('bill.html')
    
    def post(self):
        pass


class ResultPage(MethodView):
    def get(self):
        return render_template('result.html')
    
    def post(self):
        pass


class BillForm(Form):
    pass
