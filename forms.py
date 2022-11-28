from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, SelectField)
from wtforms.validators import InputRequired, Length


class CourseSimulator(FlaskForm):
    denumireCurs = StringField('Denumire Curs', validators=[InputRequired(),
                                                            Length(min=3, max=100)])
    numarOre = IntegerField('Numar Ore', validators=[InputRequired()])
    costCurs = IntegerField('Cost curs', validators=[InputRequired()])
    costLiceenta = IntegerField('Cost liceenta', validators=[InputRequired()])
    students = IntegerField('Studenti/Iteratie', validators=[InputRequired()])
    iteratii = IntegerField('Numar iteratii', validators=[InputRequired()])
    numeProfesor = StringField('Nume profesor', validators=[InputRequired(),
                                                            Length(min=3, max=100)])
    tarifOrar = IntegerField('Tarif orar profesor', validators=[InputRequired()])
    costOperational = IntegerField('Cost operational/student', validators=[InputRequired()])
    costMarketing = IntegerField('Cost marketing', validators=[InputRequired()])


class PriceSimulator(FlaskForm):
    workItem = StringField('Denumire activitate', validators=[InputRequired(), Length(min=5, max=200)])
    workItemType = SelectField('Tip activitate', choices=[('cpp', 'B2B Course'), ('py', 'Consultancy')])
    workItemTypeComplexity = SelectField('Complexity', choices=[('low', 'Low'), ('mid', 'Mid'), ('high', 'Hig')])
    workItemDuration = IntegerField('Durata activitate', validators=[InputRequired()])
