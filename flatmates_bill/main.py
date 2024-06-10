from app_views import Bill, Flatmate, PdfReport, FileShare
from app_utils import validate_float, validate_int, validate_date


def main():
    """
    Main function to prompt the user for bill and flatmate information, 
    calculate each flatmate's share of the bill, and generate a PDF report.

    Prompts the user for:
        - Total bill amount (validated as a positive float).
        - Bill period (formatted as a title case string).
        - First flatmate's name and number of days stayed (validated as a positive integer).
        - Second flatmate's name and number of days stayed (validated as a positive integer).

    Prints each flatmate's share of the bill and generates a PDF report.
    """
    # Prompt user for input
    bill_amount = validate_float("\n\n- Enter the total bill amount (USD): ")
    bill_period = validate_date(
        "\n- Enter the bill period (e.g., 'March 2024'): ")

    # Get details for the first flatmate
    name1 = input("\n\n- Enter the first flatmate's name: ").title()
    days1 = validate_int(f'  Enter the number of days "{
                         name1}" stayed in the house during "{bill_period.title()}": ')

    # Get details for the second flatmate
    name2 = input("\n\n- Enter the second flatmate's name: ").title()
    days2 = validate_int(f'  Enter the number of days "{
                         name2}" stayed in the house during "{bill_period.title()}": ')

    # Create Bill and Flatmate instances
    the_bill = Bill(amount=bill_amount, period=bill_period)
    flatmate1 = Flatmate(name=name1, days_in_house=days1)
    flatmate2 = Flatmate(name=name2, days_in_house=days2)

    # Print the payment information
    print(f'\n\n>> {flatmate1.name} pays ${
          flatmate1.pays(bill=the_bill, flatmate=flatmate2)}')
    print(f'\n>> {flatmate2.name} pays ${
          flatmate2.pays(bill=the_bill, flatmate=flatmate1)}')

    # Generate the PDF report (bill)
    pdf_bill = PdfReport(flatmate1, flatmate2, the_bill)
    pdf_bill_path = pdf_bill.generate()

    # Share the pdf bill by uploading it to filestack and get its url
    pdf_bill_url = FileShare(filepath=pdf_bill_path).share()

    # Return the url
    return pdf_bill_url


if __name__ == "__main__":
    try:
        bill_url = main()
        print(
            f'\n\n--- PDF Flatmates Bill generated successfully.\n\n    You can find it here: "{bill_url}" ---\n\n')
    except Exception as e:
        print(f'\n\n--- An error occured: "{e}" ---\n\n')
