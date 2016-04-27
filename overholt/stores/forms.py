# -*- coding: utf-8 -*-
"""
    overholt.stores.forms
    ~~~~~~~~~~~~~~~~~~~~~

    Store forms
"""

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Optional

__all__ = ['NewStoreForm', 'UpdateStoreForm']


class NewStoreForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zip_code = StringField('Zip Code', validators=[DataRequired()])


class UpdateStoreForm(Form):
    name = StringField('Name', validators=[Optional()])
    address = StringField('Address', validators=[Optional()])
    city = StringField('City', validators=[Optional()])
    state = StringField('State', validators=[Optional()])
    zip_code = StringField('Zip Code', validators=[Optional()])
