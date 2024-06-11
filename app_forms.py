# `flask_wtf.FlaskForm` automatically includes a CSRF token field in the form, making it easy to protect forms against CSRF attacks without having to manually add the CSRF token field to each form like in `wtforms.Form`
from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField, DecimalField, IntegerField
from wtforms.validators import DataRequired, NumberRange, InputRequired, Length, Regexp, ValidationError
from datetime import datetime


class FutureDateError(Exception):
    pass


class BillForm(FlaskForm):
    """
    Form class for bill details and flatmates information.

    Attributes:
        amount (DecimalField): Field for entering the bill amount.
        period (StringField): Field for entering the bill period.
        name1 (StringField): Field for entering the name of the first flatmate.
        days_in_house1 (IntegerField): Field for entering the number of days the first flatmate stayed in the house.
        name2 (StringField): Field for entering the name of the second flatmate.
        days_in_house2 (IntegerField): Field for entering the number of days the second flatmate stayed in the house.
        button (SubmitField): Button for submitting the form.
    """

    def validate_bill_period(form, field):
        try:
            bill_period_date = datetime.strptime(field.data.title(), "%B %Y")

            if bill_period_date > datetime.now():
                raise FutureDateError("Period cannot be in the future.")

        except (ValueError, TypeError):
            raise ValidationError(
                "Period must be in the format 'Month Year' (e.g., 'March 2024').")

        except FutureDateError as e:
            raise ValidationError(str(e))

    amount = DecimalField(
        label="Bill Amount",
        validators=[
            InputRequired(message="Amount is required."),
            NumberRange(
                min=1, message="Amount must be a positive number.")
        ],
        render_kw={"placeholder": "e.g., 400.0"}
    )

    period = StringField(
        label="Bill Period",
        validators=[
            DataRequired(message="Period is required."),
            validate_bill_period
        ],

        render_kw={"placeholder": "e.g., May 2024"}
    )

    name1 = StringField(
        label="Flatmate A - Name",
        validators=[
            DataRequired(message="Name is required."),
            Length(
                min=1, max=20, message="Name must be between 1 and 20 characters."),
            Regexp('^ *[a-zA-Z]+ *$',  # 0 or more space char before and after
                   message="Name can only contain letters.")
        ],
        render_kw={"placeholder": "e.g., Alex"}
    )

    days_in_house1 = IntegerField(
        label="Flatmate A - Days in the house",
        validators=[
            InputRequired(
                message="Number of days in house is required."),
            NumberRange(
                min=0, max=31, message="Number of days in house must be a positive number.")
        ],
        render_kw={"placeholder": "e.g., 24"}
    )

    name2 = StringField(
        label="Flatmate B - Name",
        validators=[
            DataRequired(message="Name is required."),
            Length(
                min=1, max=20, message="Name must be between 1 and 20 characters."),
            Regexp('^ *[a-zA-Z]+ *$',  # 0 or more space char before and after
                   message="Name can only contain letters.")
        ],
        render_kw={"placeholder": "e.g., Michael"}
    )
    days_in_house2 = IntegerField(
        label="Flatmate B - Days in the house",
        validators=[
            InputRequired(
                message="Number of days in house is required."),
            NumberRange(
                min=0, max=31, message="Number of days in house must be a positive number.")
        ],
        render_kw={"placeholder": "e.g., 29"}
    )

    submit = SubmitField("Calculate")
