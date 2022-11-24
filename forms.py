from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, SubmitField)
from wtforms.validators import InputRequired, Length


class CourseSimulator(FlaskForm):
    denumireCurs = StringField('Denumire Curs', validators=[InputRequired(),
                                                            Length(min=3, max=100)])
    numarOre = IntegerField('Numar Ore', validators=[InputRequired()])
    costCurs = IntegerField('Cost curs', validators=[InputRequired()])
    costCompetitie = IntegerField('Avg. cost/h competitie', validators=[InputRequired()])
    costLiceenta = IntegerField('Cost liceenta', validators=[InputRequired()])
    students = IntegerField('Studenti/Iteratie', validators=[InputRequired()])
    iteratii = IntegerField('Numar iteratii', validators=[InputRequired()])
    numeProfesor = StringField('Nume profesor', validators=[InputRequired(),
                                                            Length(min=3, max=100)])
    tarifOrar = IntegerField('Tarif orar profesor', validators=[InputRequired()])
    costOperational = IntegerField('Cost operational/student', validators=[InputRequired()])
    costMarketing = IntegerField('Cost marketing', validators=[InputRequired()])
