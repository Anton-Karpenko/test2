import pytest
from django.conf import settings
from rest_framework.test import APIRequestFactory

from apps.users.tests.factories import UserFactory
from apps.menu_items.tests.factories import MenuItemFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> settings.AUTH_USER_MODEL:
    return UserFactory()


@pytest.fixture
def request_factory() -> APIRequestFactory:
    return APIRequestFactory()


@pytest.fixture
def menu_item():
    return MenuItemFactory()
