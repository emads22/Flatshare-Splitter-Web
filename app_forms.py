from wtforms import Form, StringField, SubmitField


class BillForm(Form):
    amount = StringField("Bill Amount: ", default="400.0")
    period = StringField("Bill Period: ", default="May 2024")

    name1 = StringField("Name: ", default="Alex")
    days_in_house1 = StringField("Days in the house: ", default="24")

    name2 = StringField("Name: ", default="Michael")
    days_in_house2 = StringField("Days in the house: ", default="29")

    button = SubmitField("Calculate")
