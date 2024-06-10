import os
import webbrowser
from fpdf import FPDF
from filestack import Client
# from constants import *


class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """

    def __init__(self, amount, period) -> None:
        """
        Initialize a Bill instance.

        Args:
            amount (float): The total amount of the bill.
            period (str): The period for which the bill is generated (e.g., 'March 2024').
        """
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays a share of the bill.
    """

    def __init__(self, name, days_in_house) -> None:
        """
        Initialize a Flatmate instance.

        Args:
            name (str): The name of the flatmate.
            days_in_house (int): The number of days the flatmate stayed in the house during the billing period.
        """
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill: Bill, flatmate: 'Flatmate') -> float:
        """
        Calculate the amount this flatmate needs to pay based on their share of the days stayed.

        We put single quotes around Flatmate ('Flatmate') in the type hint for the flatmate parameter to indicate that it's a string literal representing the class name, rather than an instance of the Flatmate class itself cz here the Flatmate class has not yet been fully defined, so we can't use it as a type hint directly.

        Args:
            bill (Bill): The bill object containing the total amount and period.
            flatmate (Flatmate): The other flatmate sharing the bill.

        Returns:
            float: The amount this flatmate needs to pay.
        """
        # Calculate the weight of this flatmate's share of the bill
        # This is done by dividing the number of days this flatmate was in the house
        # by the total number of days both flatmates were in the house
        weight = self.days_in_house / \
            (self.days_in_house + flatmate.days_in_house)

        # Calculate the amount this flatmate needs to pay
        # This is done by multiplying the total bill amount by the weight calculated above
        amount_to_pay = bill.amount * weight

        return round(amount_to_pay, 2)


# class PdfReport(FPDF):
#     """
#     Creates a PDF file that contains data about the flatmates such as their names, 
#     their due amounts, and the period of the bill.
#     """

#     def __init__(self, flatmate1: Flatmate, flatmate2: Flatmate, bill: Bill) -> None:
#         """
#         Initialize a PdfReport instance.

#         Args:
#             flatmate1 (Flatmate): The first flatmate.
#             flatmate2 (Flatmate): The second flatmate.
#             bill (Bill): The bill object containing the total amount and period.
#         """
#         # Initialize the parent class with specified orientation, unit, and format.
#         # Orientation 'P' is for Portrait mode.
#         # Unit 'pt' is points, a common unit for print documents, typically 1/72 of an inch.
#         # Format 'A4' is a standard paper size.
#         # Using 'pt' (points) is often better than 'px' (pixels) in print documents.
#         # Points are a physical measurement unit (1 point = 1/72 inch) and provide consistent sizing
#         # across different printers and display resolutions, ensuring the document looks as expected
#         # when printed. Pixels, on the other hand, are more suited for digital displays and can vary
#         # in size depending on screen resolution, making them less reliable for print consistency.
#         super().__init__(orientation='P', unit='pt', format='A4')  # 12pt = 16px
#         self.flatmate1 = flatmate1
#         self.flatmate2 = flatmate2
#         self.bill = bill

#     def generate(self) -> str:
#         # Define variables to be written in the PDF bill
#         bill_period = self.bill.period.title()
#         bill_amount = self.bill.amount
#         flatmate1_name = self.flatmate1.name
#         flatmate1_payment = self.flatmate1.pays(self.bill, self.flatmate2)
#         flatmate2_name = self.flatmate2.name
#         flatmate2_payment = self.flatmate2.pays(self.bill, self.flatmate1)

#         # Start a new page in the PDF
#         self.add_page()

#         # Set the font for the header
#         self.set_font(family='Arial', style='B', size=24)

#         # Add image
#         self.image(str(BILL_LOGO), w=30, h=30)

#         # Add the main title of the document
#         self.cell(w=0, h=80, txt="Flatmates Bill", align='C', ln=1)

#         # Add the period label and value
#         self.set_font_size(22)  # Set font size for the period label
#         self.cell(w=100, h=30, txt=f"Period:", ln=0)
#         self.set_font(family='Courier')  # Set font for the period value
#         self.cell(w=150, h=30, txt=f"{bill_period}", ln=1)

#         # Add the total amount label and value
#         self.set_font(family='Arial', style='B')  # Reset font for amount
#         self.cell(w=180, h=30, txt=f"Total Amount:", ln=0)
#         self.set_font(family='Courier')  # Set font for the amount value
#         self.cell(w=100, h=30, txt=f"${bill_amount}", ln=1)
#         self.ln()  # Add a line break

#         # Add the body of flatmates names and respective payment amounts
#         self.set_font(family='Arial', size=20)  # Set font for 1st name
#         self.cell(w=100, h=30, txt=f"- {flatmate1_name}:", ln=0)
#         self.set_font(family='Courier')  # Set font for the payment value
#         self.cell(w=100, h=30, txt=f"${flatmate1_payment}", ln=1)

#         self.set_font(family='Arial')  # Reset font for 2nd name
#         self.cell(w=100, h=30, txt=f"- {flatmate2_name}:", ln=0)
#         self.set_font(family='Courier')  # Set font for the payment value
#         self.cell(w=100, h=30, txt=f"${flatmate2_payment}", ln=1)

#         # Reset font to Arial for further content if needed
#         self.set_font(family='Arial')

#         # Define the output file path based on the bill period
#         filename = self.bill.period.title().replace(" ", "_")
#         output_filepath = BILLS / f'{filename}_Bill.pdf'

#         # Save the PDF to the specified file path
#         self.output(str(output_filepath))

#         # Automatically open the created PDF file (bill) to view it using the default PDF viewer on the system
#         webbrowser.open(str(output_filepath))

#         # Return the pdf report output path as str
#         return str(output_filepath)


# class FileShare:
#     """
#     A class used to share files using the Filestack API.

#     Attributes:
#         filepath (str): The path to the file to be shared.
#         api_key (str): The API key for the Filestack API (default is FILESTACK_API_KEY).
#     """

#     def __init__(self, filepath: str, api_key: str = FILESTACK_API_KEY) -> None:
#         """
#         Initializes a FileShare instance.

#         Args:
#             filepath (str): The path to the file to be shared.
#             api_key (str, optional): The API key for the Filestack API (default is FILESTACK_API_KEY).
#         """
#         self.filepath = filepath
#         self.api_key = api_key

#     def share(self) -> str:
#         """
#         Shares the file using the Filestack API and returns the URL of the shared file.

#         Returns:
#             str: The URL of the shared file.

#         Raises:
#             Exception: If an error occurs during file upload.
#         """
#         try:
#             client = Client(self.api_key)
#             pdf_filelink = client.upload(filepath=self.filepath)
#             return pdf_filelink.url
#         except Exception as e:
#             raise Exception(f"An error occurred while sharing the file: {e}")
