from flask import render_template, request, redirect, url_for, flash
from flask.views import MethodView
from app_forms import BillForm
from flatmates_bill import classes as fb_classes
from app_utils import extra_validation


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

        # Server-Side Validation: It performs server-side form validation, ensuring that even if JavaScript is disabled on the client side, the validation logic is enforced.

        if not bill_form.validate():
            flash('Please correct the errors in the form and try again.')
            # Pass the form object back to the form page for correction
            return render_template('bill_form.html', billform=bill_form)
        
        # If the form passed standard validation, perform custom validation
        extra_validated, error_message = extra_validation(bill_form)
        if not extra_validated:
            flash(error_message)
            # Pass the form object back to the form page for correction
            return render_template('bill_form.html', billform=bill_form)

        try:
            bill_amount = float(bill_form.amount.data)
            bill_period = bill_form.period.data.title()

            name1 = bill_form.name1.data.title()
            days1 = int(bill_form.days_in_house1.data)

            name2 = bill_form.name2.data.title()
            days2 = int(bill_form.days_in_house2.data)

            # Create Bill and Flatmate instances
            the_bill = fb_classes.Bill(amount=bill_amount, period=bill_period)
            flatmate1 = fb_classes.Flatmate(name=name1, days_in_house=days1)
            flatmate2 = fb_classes.Flatmate(name=name2, days_in_house=days2)

            return render_template(
                'result.html',
                bill=the_bill,
                name1=name1,
                amount1=flatmate1.pays(bill=the_bill, flatmate=flatmate2),
                name2=name2,
                amount2=flatmate2.pays(bill=the_bill, flatmate=flatmate1)
            )

        except ValueError as e:
            flash(f"An error occurred while processing the form: {e}")
            # Redirect to form page if there's an error
            return redirect(url_for('bill_form_page'))





        