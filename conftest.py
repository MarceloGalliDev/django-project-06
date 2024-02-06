import pytest
from pytest_factorybot import register
from core_apps.users.tests.factories import UserFactory


register(UserFactory)


@pyteste.fixture
def normal_user(db, user_factory):
    new_user = user_factory.create()
    return new_user


@pyteste.fixture
def super_user(db, user_factory):
    new_user = user_factory.create(is_staff=True, is_superuser=True)
    return new_user
