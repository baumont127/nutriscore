from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email, Length, ValidationError



class NutriscoreForm(FlaskForm):
    energie = IntegerField("Energie", validators=[DataRequired()])
    matieres_grasses = IntegerField("matieres_grasses")
    acides_gras_satures = IntegerField("acides_gras_satures")
    sucres = IntegerField("sucres")
    fibres = IntegerField("fibres")
    proteines = IntegerField("proteines")
    sel = IntegerField("sel")
    sodium = IntegerField("sodium")
    fruits = IntegerField("fruits")
    submit = SubmitField("S'inscrire")

