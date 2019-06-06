from django.urls import path

from .api.views import ListMenuItemsAPIView

app_name = 'menu_items'

urlpatterns = [
    path('', ListMenuItemsAPIView.as_view(), name='list'),
]
