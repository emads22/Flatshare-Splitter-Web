from flask.views import MethodView
from app_forms import BillForm
from flask import render_template, request


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')

    def post(self):
        pass


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form.html', billform=bill_form)

    def post(self):
        pass


class ResultPage(MethodView):
    def post(self):
        bill_form = BillForm(request.form)
        x = bill_form.amount.data
        y = bill_form.period.data

        return render_template('result.html', x=x, y=y)
