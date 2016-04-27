# -*- coding: utf-8 -*-
"""
    tests.factories
    ~~~~~~~~~~~~~~~

    Overholt test factories module
"""
import factory

from datetime import datetime
from flask_security.utils import encrypt_password
from . import orm_session

from overholt.models import *


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
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

    email = factory.Sequence(lambda n: 'user{0}@overholt.com'.format(n))
    password = factory.LazyAttribute(lambda a: encrypt_password('password'))
    last_login_at = datetime.utcnow()
    current_login_at = datetime.utcnow()
    last_login_ip = '127.0.0.1'
    current_login_ip = '127.0.0.1'
    login_count = 1
    active = True

    @factory.post_generation
    def roles(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for role in extracted:
                self.groups.add(role)


class StoreFactory(BaseFactory):
    class Meta:
        model = Store

    name = factory.Sequence(lambda n: 'Store Number {0}'.format(n))
    address = '123 Overholt Alley'
    city = 'Overholt'
    state = 'New York'
    zip_code = '12345'


class ProductFactory(BaseFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: 'Product Number {0}'.format(n))


class CategoryFactory(BaseFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: 'Category {0}'.format(n))
