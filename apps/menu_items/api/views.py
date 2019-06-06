from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics

from apps.menu_items.api import docs
from apps.menu_items.models import MenuItem
from .serializers import MenuItemSerializer


@method_decorator(name='get', decorator=swagger_auto_schema(**docs.list_menu_items))
class ListMenuItemsAPIView(generics.ListAPIView):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()
