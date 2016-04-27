# -*- coding: utf-8 -*-
"""
    overholt.products.forms
    ~~~~~~~~~~~~~~~~~~~~~~~

    Product forms
"""

from flask_wtf import Form
from wtforms import StringField, SelectMultipleField
from wtforms.validators import DataRequired, Optional

from ..services import products

__all__ = ['NewProductForm', 'UpdateProductForm']


class ProductFormMixin(object):

    def __init__(self, *args, **kwargs):
        super(ProductFormMixin, self).__init__(*args, **kwargs)
        self.categories.choices = [(c.id, c.name) for c in products.categories.all()]


class NewProductForm(ProductFormMixin, Form):
    name = StringField('Name', validators=[DataRequired()])
    categories = SelectMultipleField(
        'Categories', coerce=int, validators=[DataRequired()])


class UpdateProductForm(ProductFormMixin, Form):
    name = StringField('Name', validators=[Optional()])
    categories = SelectMultipleField(
        'Categories', coerce=int, validators=[Optional()])
