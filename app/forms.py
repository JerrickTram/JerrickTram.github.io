from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddWordForm(FlaskForm):
    swedish_word = StringField('Swedish Word', validators=[DataRequired()])
    english_translation = StringField('Translation', validators=[DataRequired()])
    tags = StringField('Tags')
    submit = SubmitField('Add Word')

class QuizForm(FlaskForm):
    answer = StringField('Your Answer', validators=[DataRequired()])
    submit = SubmitField('Submit')