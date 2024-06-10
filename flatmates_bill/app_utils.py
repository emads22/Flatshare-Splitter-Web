from datetime import datetime


def validate_float(prompt):
    """
    Prompt the user to enter a positive floating-point number.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        float: The validated positive floating-point number.

    Raises:
        ValueError: If the input is not a valid float or is a negative number.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("\n-- Invalid input. Please enter a positive number. --\n")


def validate_int(prompt):
    """
    Prompt the user to enter a positive integer.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        int: The validated positive integer.

    Raises:
        ValueError: If the input is not a valid integer or is a negative number.
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("\n-- Invalid input. Please enter a positive integer. --\n")


def validate_date(prompt):
    """
    Validates the bill period entered by the user to ensure it's not in the future.

    Args:
        prompt (str): The prompt message asking the user to enter the bill period.

    Returns:
        str: A string representing the validated bill period in the format 'Month Year' (e.g., 'March 2024').

    Raises:
        ValueError: If the entered period is not in the correct format.
    """
    current_date = datetime.now()
    while True:
        bill_period = input(prompt).title()
        try:
            # Try parsing the entered bill period into a datetime object
            bill_period_date = datetime.strptime(bill_period, "%B %Y")
            if bill_period_date > current_date:
                # Check if the entered period is in the future
                print(
                    "\n-- Error: Bill period cannot be in the future. Please enter a valid period. --\n")
            else:
                # If the period is valid, format it as a string and return
                bill_period_str = datetime.strftime(
                    bill_period_date, "%B %Y")
                return bill_period_str
        except ValueError:
            print("\n-- Error: Please enter a valid bill period in the format 'Month Year' (e.g., 'March 2024'). --\n")
