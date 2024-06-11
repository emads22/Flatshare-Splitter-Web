from datetime import datetime
from flatmates_bill import classes as fb_classes


def generate_and_upload_PDF_bill(flatmate1, flatmate2, the_bill):
    """
    Generates a PDF report for the bill and uploads it to Filestack.

    Args:
        flatmate1 (Flatmate): The first flatmate involved in the bill.
        flatmate2 (Flatmate): The second flatmate involved in the bill.
        the_bill (Bill): The bill containing the total amount and period.

    Returns:
        tuple: A tuple containing either:
               - (str, None): The URL of the uploaded PDF bill if successful.
               - (None, str): An error message if the process fails.
    """
    try:
        # Generate the PDF report (bill)
        pdf_bill = fb_classes.PdfReport(flatmate1, flatmate2, the_bill)
        pdf_bill_path = pdf_bill.generate()

        # Share the PDF bill by uploading it to Filestack and get its URL
        bill_url = fb_classes.FileShare(filepath=pdf_bill_path).share()

        return bill_url, None

    except Exception as e:
        # Log the error and return a meaningful message
        error_message = f"An error occurred during PDF bill generation or file upload"
        print(f'\n\n--- {error_message}: {e} ---\n\n')  # Use logging in production
        return None, error_message


def extra_validation(bill_form):
    """
    Perform additional validation on the BillForm fields.

    Args:
        bill_form (BillForm): The form containing bill details and information about the days 
                              two people stayed in the house.

    Returns:
        tuple: A tuple containing either data or an empty dictionary, and an error message string.
               ({}, None) if validation is successful with validated data dictionary.
               (None, error_message) if validation fails with error messages concatenated.
    """
    error_message = []

    # Validate bill amount
    try:
        bill_amount = float(bill_form.amount.data)
        if bill_amount <= 0:
            error_message.append("-- 'Bill Amount' must be a positive number.")
    except (ValueError, TypeError):
        error_message.append("-- 'Bill Amount' must be a positive number.")

    # Validate bill period
    try:
        bill_period = bill_form.period.data.title()
        bill_period_date = datetime.strptime(bill_period, "%B %Y")
        current_date = datetime.now()
        if bill_period_date > current_date:
            error_message.append("-- 'Bill Period' cannot be in the future.")
    except (ValueError, TypeError):
        error_message.append(
            "-- 'Bill Period' must be in the format 'Month Year' (e.g., 'March 2024').")

    # Validate names
    name1 = bill_form.name1.data.title()
    name2 = bill_form.name2.data.title()
    if not name1 or not name1.strip() or not name2 or not name2.strip():
        error_message.append("-- Name field is required.")
    if not name1.strip().isalpha():
        error_message.append(
            "-- 'Flatmate A Name' must contain only alphabetic characters.")
    if not name2.strip().isalpha():
        error_message.append(
            "-- 'Flatmate B Name' must contain only alphabetic characters.")

    # Validate days in house
    try:
        days1 = int(bill_form.days_in_house1.data)
        days2 = int(bill_form.days_in_house2.data)
        if days1 < 0 or days2 < 0:
            error_message.append(
                "-- 'Days in House' must be a positive integer.")
    except (ValueError, TypeError):
        error_message.append("-- 'Days in House' must be a positive integer.")

    if error_message:
        return None, "\n".join(error_message)

    data = {
        'bill_amount': bill_amount,
        'bill_period': bill_period,
        'name1': name1,
        'name2': name2,
        'days1': days1,
        'days2': days2
    }
    return data, None
