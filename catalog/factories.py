from factory import django, Faker, fuzzy

from .models import Category, Product

COLORS = (
    'blue',
    'red',
    'yellow',
    'green',
    'black',
    'orange',
)


class CategoryFactory(django.DjangoModelFactory):
    class Meta:
        model = Category

    name = Faker('company')
    slug = name
    is_active = True


class ProductFactory(django.DjangoModelFactory):
    class Meta:
        model = Product

    name = Faker('word')
    slug = name
    description = Faker('sentence')
    category = fuzzy.FuzzyChoice(choices=Category.objects.all())
    is_active = True
    image = django.ImageField(
        width=1000,
        height=1000,
        color=fuzzy.FuzzyChoice(choices=COLORS)
    )
    price = fuzzy.FuzzyDecimal(80, 450, 1)
