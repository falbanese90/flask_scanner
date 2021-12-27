from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired

class StockForm(FlaskForm):
    stock = StringField(label='Stock', validators=[DataRequired(), Length(max=5)])
    submit = SubmitField(label='Go')