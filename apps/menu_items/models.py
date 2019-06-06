import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class MenuItem(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        _("Dish name"),
        max_length=255
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2
    )

    class Meta:
        db_table = 'menu_item'
        ordering = ('-created',)

    def __str__(self):
        return self.name
