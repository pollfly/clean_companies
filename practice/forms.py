from wtforms import Form, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(Form):
    search = StringField('Search for music:' [DataRequired()])
    submit = SubmitField('Search',
                         render_kw={'class': 'btn btn-success btn-block'})



# class MusicSearchForm(Form):
#     choices = [('Artist', 'Artist'),
#                ('Album', 'Album'),
#                ('Publisher', 'Publisher')]
#     select = SelectField('Search for music:', choices=choices)
#     search = StringField('')