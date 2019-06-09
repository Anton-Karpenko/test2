import pytest
from django.urls import reverse, resolve

pytestmark = pytest.mark.django_db


def test_list():
    assert reverse("menu_items:list") == "/api/menu-items/"
    assert resolve("/api/menu-items/").view_name == "menu_items:list"
