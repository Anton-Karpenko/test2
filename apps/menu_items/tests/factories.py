from factory import DjangoModelFactory, Faker
from factory.fuzzy import FuzzyDecimal
from apps.menu_items.models import MenuItem


class MenuItemFactory(DjangoModelFactory):
    name = Faker('sentence', nb_words=1)
    price = FuzzyDecimal(1, 10000)

    class Meta:
        model = MenuItem
