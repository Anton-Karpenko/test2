from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MenuItemsConfig(AppConfig):
    name = "apps.menu_items"
    verbose_name = _("Menu items")
