from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, URL, InputRequired, Optional

class AddPetForm(FlaskForm):
    """Form for adding a new pet"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_url =  StringField("Photo Url", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing a pet"""

    photo_url =  StringField("Photo Url", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available?", validators=[Optional("Do you want to change availability?")])