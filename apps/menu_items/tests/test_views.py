import pytest
from rest_framework import status

from apps.base.test_mixins import GetResponseMixin
from apps.conftest import MenuItemFactory
from apps.menu_items.api.views import ListMenuItemsAPIView

pytestmark = pytest.mark.django_db


class TestListMenuItemsAPIView(GetResponseMixin):
    URL = 'menu_items:list'
    VIEW = ListMenuItemsAPIView

    def test_get_list(self, request_factory):
        self.set_data()
        response = self.get_response(request_factory)
        assert response.status_code == status.HTTP_200_OK

    @staticmethod
    def set_data():
        [MenuItemFactory() for i in range(3)]
