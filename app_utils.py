from datetime import datetime


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
        bill_period = datetime.strptime(bill_form.period.data.title(), "%B %Y")
        current_date = datetime.now()
        if bill_period > current_date:
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
            "-- 'First Flatmate Name' must contain only alphabetic characters.")
    if not name2.strip().isalpha():
        error_message.append(
            "-- 'Second Flatmate Name' must contain only alphabetic characters.")

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
        'bill_period': bill_period.strftime("%B %Y"),
        'name1': name1,
        'name2': name2,
        'days1': days1,
        'days2': days2
    }
    return data, None
