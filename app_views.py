from flask import render_template, request, redirect, url_for, flash
from flask.views import MethodView
from app_forms import BillForm
from flatmates_bill import classes as fb_classes
from app_utils import extra_validation


class HomePage(MethodView):
    """
    View class for the home page.

    Methods:
        get(): Handles GET requests and renders the home page template.
        post(): Handles POST requests. Currently not implemented.
    """

    def get(self):
        """
        Handle GET requests and render the home page template.

        Returns:
            A rendered template for the home page.
        """
        return render_template('index.html')

    def post(self):
        """
        Handle POST requests. Currently not implemented.
        """
        pass


class BillFormPage(MethodView):
    """
    View class for the bill form page.

    Methods:
        get(): Handles GET requests, initializes the BillForm, and renders the bill form template.
        post(): Handles POST requests. Currently not implemented.
    """

    def get(self):
        """
        Handle GET requests, initialize the BillForm, and render the bill form template.

        Returns:
            A rendered template for the bill form page with an initialized BillForm.
        """
        bill_form = BillForm()  # Initialize the bill form
        return render_template('bill_form.html', billform=bill_form)

    def post(self):
        """
        Handle POST requests by processing form data, performing validation, and rendering the result template.

        Returns:
            Rendered template for the same Bill_form page with calculated bill details.
        """
        bill_form = BillForm(request.form)

        # Server-Side Validation: Perform server-side form validation
        if not bill_form.validate():
            flash('Please correct the errors in the form and try again.')
            # Pass the form object back to the form page for correction
            return render_template('bill_form.html', billform=bill_form)

        # If the form passed standard validation, perform custom validation
        extra_validated_data, error_message = extra_validation(bill_form)
        if extra_validated_data is None:
            flash(error_message)
            # Pass the form object back to the form page for correction
            return render_template('bill_form.html', billform=bill_form)

        try:
            # Extract data from the form
            bill_amount = extra_validated_data['bill_amount']
            bill_period = extra_validated_data['bill_period']
            name1 = extra_validated_data['name1']
            name2 = extra_validated_data['name2']

            # Create Bill and Flatmate instances
            the_bill = fb_classes.Bill(amount=bill_amount, period=bill_period)
            flatmate1 = fb_classes.Flatmate(
                name=name1, days_in_house=extra_validated_data['days1'])
            flatmate2 = fb_classes.Flatmate(
                name=name2, days_in_house=extra_validated_data['days2'])

            # Calculate bill shares for each flatmate
            amount1 = flatmate1.pays(bill=the_bill, flatmate=flatmate2)
            amount2 = flatmate2.pays(bill=the_bill, flatmate=flatmate1)

            # Render the result template with calculated bill details
            return render_template(
                'bill_form.html',
                billform=BillForm(),
                result=True,
                bill=the_bill,
                name1=name1,
                amount1=amount1,
                name2=name2,
                amount2=amount2
            )

        except ValueError as e:
            flash(f"An error occurred while processing the form: {e}")
            # Redirect to the form page if there's an error
            return redirect(url_for('bill_form_page'))


class ResultPage(MethodView):
    """
    View class for the result page.

    Methods:
        post(): Handles POST requests by processing form data, performing validation,
                and rendering the result template.
    """

    def post(self):
        """
        Handle POST requests by processing form data, performing validation, and rendering the result template.

        Returns:
            Rendered template for the result page with calculated bill details.
        """
        bill_form = BillForm(request.form)

        # Server-Side Validation: Perform server-side form validation
        if not bill_form.validate():
            flash('Please correct the errors in the form and try again.')
            # Pass the form object back to the form page for correction
            return render_template('bill_form.html', billform=bill_form)

        # If the form passed standard validation, perform custom validation
        extra_validated_data, error_message = extra_validation(bill_form)
        if extra_validated_data is None:
            flash(error_message)
            # Pass the form object back to the form page for correction
            return render_template('bill_form.html', billform=bill_form)

        try:
            # Extract data from the form
            bill_amount = extra_validated_data['bill_amount']
            bill_period = extra_validated_data['bill_period']
            name1 = extra_validated_data['name1']
            name2 = extra_validated_data['name2']

            # Create Bill and Flatmate instances
            the_bill = fb_classes.Bill(amount=bill_amount, period=bill_period)
            flatmate1 = fb_classes.Flatmate(
                name=name1, days_in_house=extra_validated_data['days1'])
            flatmate2 = fb_classes.Flatmate(
                name=name2, days_in_house=extra_validated_data['days2'])

            # Calculate bill shares for each flatmate
            amount1 = flatmate1.pays(bill=the_bill, flatmate=flatmate2)
            amount2 = flatmate2.pays(bill=the_bill, flatmate=flatmate1)

            # Render the result template with calculated bill details
            return render_template(
                'result.html',
                bill=the_bill,
                name1=name1,
                amount1=amount1,
                name2=name2,
                amount2=amount2
            )

        except ValueError as e:
            flash(f"An error occurred while processing the form: {e}")
            # Redirect to the form page if there's an error
            return redirect(url_for('bill_form_page'))
