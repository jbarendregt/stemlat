from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField, DecimalField, IntegerField
#from flask_pagedown.fields import PageDownField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from ..models import Theme

#from ..decorators import clients_dropdown

#from ..models import Role, User


class PartyForm(FlaskForm):
    party_name = StringField('Name party', validators=[Length(0, 64), Required()])
    submit = SubmitField('Submit')

class ThemeForm(FlaskForm):
    theme_name = StringField('Name theme', validators=[Length(0, 64), Required()])
    submit = SubmitField('Submit')

class TopicForm(FlaskForm):
    topic_name = StringField('Name topic', validators=[Length(0, 64), Required()])
    theme =  SelectField('Theme', coerce=int)
    submit = SubmitField('Submit')

class IndexForm(FlaskForm):
    party = SelectField('Partij', coerce=int)
    theme = SelectField('Thema', coerce=int)
    submit = SubmitField('Submit')
