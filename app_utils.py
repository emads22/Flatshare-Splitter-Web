from datetime import datetime

def extra_validation(bill_form):
    error_message = ""

    # Validate bill amount
    try:
        bill_amount = float(bill_form.amount.data)
        if bill_amount <= 0:
            raise ValueError
    except (ValueError, TypeError):
        error_message += "-- 'Bill Amount' must be a positive number.\n"

    # Validate bill period
    current_date = datetime.now()
    bill_period = bill_form.period.data.title()
    try:
        bill_period_date = datetime.strptime(bill_period, "%B %Y")
        if bill_period_date > current_date:
            error_message += "-- 'Bill Period' cannot be in the future.\n"
    except (ValueError, TypeError):
        error_message += "-- 'Bill Period' mus be in the format 'Month Year' (e.g., 'March 2024').\n"

    # Validate names
    name1 = bill_form.name1.data
    name2 = bill_form.name2.data
    if not name1 or not name1.strip() or not name2 or not name2.strip():
        error_message += "-- Name field is required.\n"
    if not name1.strip().isalpha():
        error_message += "-- 'First Flatmate Name' must contain only alphabetic characters.\n"
    if not name2.strip().isalpha():
        error_message += "-- 'Second Flatmate Name' must contain only alphabetic characters.\n"

    # Validate days in house
    try:
        days1 = int(bill_form.days_in_house1.data)
        days2 = int(bill_form.days_in_house2.data)
        if days1 < 0 or days2 < 0:
            raise ValueError
    except (ValueError, TypeError):
        error_message += "- 'Days in House' must be a positive integer.\n"

    if error_message:
        return False, error_message.strip()

    return True, None
