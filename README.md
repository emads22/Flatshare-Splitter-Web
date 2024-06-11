# Flatshare Splitter Web 

## Overview
Flatshare Splitter Web, initially a Python CLI (Command-Line Interface) application, has been upgraded to a web application using Flask. The web application continues to fairly split the utility bill among flatmates based on the number of days they stayed in the house during the billing period. The application leverages Object-Oriented Programming (OOP) principles to enhance modularity and maintainability, and now offers a user-friendly web interface for a better user experience.

The application also shares the generated PDF report using the Filestack API. However, users can modify the code to use any other cloud service for file sharing. The PDF bill design is basic and can be customized further depending on user preference and needs.

## Features
- **Bill Calculation:** Calculate the share of the bill each flatmate needs to pay based on their days of stay.
- **PDF Report Generation:** Generate a PDF report summarizing the bill details and each flatmate's share.
- **User Input Validation:** Ensure that user inputs are correctly formatted and valid.
- **File Sharing:** Share the generated PDF report using the Filestack API.
- **Customizable File Sharing:** Shares the generated PDF report using the Filestack API, with the option to modify the code for using other cloud services.
- **Error Handling:** Gracefully handle errors during the file-sharing process.
- **Web Interface:** User-friendly web interface to enter bill details and view results.
- **Session Management:** Manage user sessions to keep track of bill calculation and report generation.

## Setup
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/emads22/Flatshare-Splitter-Web.git
   ```
2. **Navigate to the Project Folder:**
   ```sh
   cd Flatshare-Splitter
   ```
3. **Ensure Python 3.x is Installed:** Check your Python version using:
   ```sh
   python --version
   ```
4. **Install Required Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
5. **Configure Necessary Parameters in constants.py:**
   Edit `flatshare_splitter/constants.py` to set any required constants for the project, such as `FILESTACK_API_KEY`.

## Usage
1. **Run the Web Application:**
   ```sh
   flask run
   ```
    or

    ```sh
    python app.py
    ```
2. **Open the Web Application:**
   Open your web browser and go to http://127.0.0.1:5000.
3. **Enter Bill Details:**
   Fill in the form with the total bill amount, bill period, and each flatmate's name and days stayed.
4. **View Calculation Results:**
   The web page will display each flatmate's share of the bill.
5. **Generate PDF Report:**
   A PDF report will be generated summarizing the bill details and each flatmate's share.
6. **Share the PDF Report:**
   The generated PDF report will be uploaded using the Filestack API, and a URL link to the report will be provided. If an error occurs during the file-sharing process, an error message will be displayed.

## Usage of Flask Views and Classes
The Flatshare Splitter web application utilizes Flask views and classes to maintain an object-oriented programming (OOP) structure, enhancing modularity and maintainability. By organizing routes and functionalities into classes, the application code remains organized and scalable.

## Detailed Validators and FlaskForm
Flask-WTF is employed for form handling, utilizing FlaskForm for detailed validation of user inputs. FlaskForm provides a convenient way to define forms in Flask applications, offering detailed validators for form fields such as `DataRequired`, `NumberRange`, `Length`, and more.

## Advantages of FlaskForm over Traditional Forms
Using FlaskForm offers several advantages over traditional forms, particularly in terms of security and ease of implementation:

1. **CSRF Protection:** FlaskForm automatically generates and validates CSRF tokens for each form, providing protection against CSRF attacks without requiring manual implementation. This significantly enhances the security of the application by preventing unauthorized form submissions.

2. **Simplified Validation:** FlaskForm simplifies the validation process by allowing the definition of validators directly within the form class. This results in cleaner and more readable code compared to manual validation using traditional forms.

3. **Integration with Jinja Templates:** FlaskForm seamlessly integrates with Jinja templates, simplifying the rendering of forms and handling of form submissions within templates. This integration streamlines the development process and improves code maintainability.

4. **Support for WTForms Features:** FlaskForm inherits all features of WTForms, allowing developers to leverage advanced form functionalities such as custom validators, field rendering options, and form inheritance.

Overall, FlaskForm offers a robust and secure solution for form handling in Flask applications, with built-in CSRF protection and simplified validation mechanisms, making it a preferred choice over traditional forms.

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.
