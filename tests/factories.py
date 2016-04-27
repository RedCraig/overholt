# -*- coding: utf-8 -*-
"""
    tests.factories
    ~~~~~~~~~~~~~~~

    Overholt test factories module
"""

from datetime import datetime
from factory import alchemy, LazyAttribute, Sequence, SubFactory
from flask_security.utils import encrypt_password
from . import orm_session

from overholt.models import *


class BaseFactory(alchemy.SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = orm_session.Session


class RoleFactory(BaseFactory):
    class Meta:
        model = Role

    name = 'admin'
    description = 'Administrator'


class UserFactory(BaseFactory):
    class Meta:
        model = User

    email = Sequence(lambda n: 'user{0}@overholt.com'.format(n))
    password = LazyAttribute(lambda a: encrypt_password('password'))
    last_login_at = datetime.utcnow()
    current_login_at = datetime.utcnow()
    last_login_ip = '127.0.0.1'
    current_login_ip = '127.0.0.1'
    login_count = 1
    # roles = SubFactory(RoleFactory)
    # roles = LazyAttribute(lambda _: [RoleFactory()])
    active = True


class StoreFactory(BaseFactory):
    class Meta:
        model = Store

    name = Sequence(lambda n: 'Store Number {0}'.format(n))
    address = '123 Overholt Alley'
    city = 'Overholt'
    state = 'New York'
    zip_code = '12345'


class ProductFactory(BaseFactory):
    class Meta:
        model = Product

    name = Sequence(lambda n: 'Product Number {0}'.format(n))


class CategoryFactory(alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Category
        sqlalchemy_session = orm_session.Session

    name = Sequence(lambda n: 'Category {0}'.format(n))
