from wtforms import Form, StringField, SubmitField, DecimalField, IntegerField
from wtforms.validators import DataRequired, NumberRange, InputRequired


class BillForm(Form):
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

    amount = DecimalField(
        "Bill Amount: ",
        validators=[InputRequired(message="Please enter the bill amount.")],
        render_kw={"placeholder": "e.g., 400.0"}
    )
    period = StringField(
        "Bill Period: ",
        validators=[DataRequired(message="Please enter the bill period.")],
        render_kw={"placeholder": "e.g., May 2024"}
    )

    name1 = StringField(
        "Name: ",
        validators=[DataRequired(message="Please enter a name.")],
        render_kw={"placeholder": "e.g., Alex"}
    )
    days_in_house1 = IntegerField(
        "Days in the house: ",
        validators=[InputRequired(), NumberRange(
            min=0, max=31, message="Days must be a positive number.")],
        render_kw={"placeholder": "e.g., 24"}
    )

    name2 = StringField(
        "Name: ",
        validators=[DataRequired(message="Please enter a name.")],
        render_kw={"placeholder": "e.g., Michael"}
    )
    days_in_house2 = IntegerField(
        "Days in the house: ",
        validators=[InputRequired(), NumberRange(
            min=0, max=31, message="Days must be a positive number.")],
        render_kw={"placeholder": "e.g., 29"}
    )

    button = SubmitField("Calculate")
