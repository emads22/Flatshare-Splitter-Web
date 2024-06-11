from flask import render_template, request, redirect, url_for, flash
from flask.views import MethodView
from app_forms import BillForm
from flatshare_splitter import classes as fs_classes
from flatshare_splitter import constants as fs_constants
from app_utils import generate_and_upload_PDF_bill


class IndexView(MethodView):
    """
    View class for handling the home page.

    This class provides methods to handle HTTP GET and POST requests for the
    home page of the application.

    Methods:
        get(): Renders and returns the home page template for GET requests.
        post(): Placeholder for handling POST requests. Not yet implemented.
    """

    def get(self):
        """
        Handle GET requests and render the home page template.

        This method processes GET requests by rendering the 'index.html' template
        and including the application's logo as ASCII art.

        Returns:
            Response: A Flask Response object containing the rendered home page template.
        """
        return render_template('index.html', app_logo=fs_constants.ASCII_ART)


class BillFormView(MethodView):
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
        if not bill_form.validate_on_submit():
            for field, errors in bill_form.errors.items():
                for error in errors:
                    field_label = getattr(bill_form, field).label.text
                    flash(f"Error in '{field_label}': {error}", 'danger')
            return render_template('bill_form.html', billform=bill_form)

        try:
            # Extract data from the form
            bill_amount = float(bill_form.amount.data)
            bill_period = bill_form.period.data.title()
            name1 = bill_form.name1.data.strip().title()
            days1 = int(bill_form.days_in_house1.data)
            name2 = bill_form.name2.data.strip().title()
            days2 = int(bill_form.days_in_house2.data)

            # Create Bill and Flatmate instances
            the_bill = fs_classes.Bill(amount=bill_amount, period=bill_period)
            flatmate1 = fs_classes.Flatmate(
                name=name1, days_in_house=days1)
            flatmate2 = fs_classes.Flatmate(
                name=name2, days_in_house=days2)

            # Calculate bill shares for each flatmate
            amount1 = flatmate1.pays(bill=the_bill, flatmate=flatmate2)
            amount2 = flatmate2.pays(bill=the_bill, flatmate=flatmate1)

            # Generate the PDF report (bill) and Share it by uploading it to filestack and get its url
            bill_url, error = generate_and_upload_PDF_bill(
                flatmate1, flatmate2, the_bill)

            if bill_url is None:
                flash(error, 'danger')

            # Render the result template with calculated bill details
            return render_template(
                'result.html',
                bill=the_bill,
                name1=name1,
                amount1=amount1,
                name2=name2,
                amount2=amount2,
                bill_url=bill_url
            )

            # # Render the result template with calculated bill details to the same bill_form_view
            # return render_template(
            #     'bill_form.html',
            #     billform=BillForm(),
            #     result=True,
            #     bill=the_bill,
            #     name1=name1,
            #     amount1=amount1,
            #     name2=name2,
            #     amount2=amount2
            # )

        except Exception as e:
            flash(f"An error occurred while processing the form: {e}")
            # Redirect to the form page if there's an error
            return redirect(url_for('bill_form_view'))
