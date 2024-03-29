from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BaseAppConfig(AppConfig):
    name = "apps.base"
    verbose_name = _("Base")
