from django.core.management import BaseCommand
from catalog.factories import CategoryFactory, ProductFactory
from catalog.models import Category, Product
from loguru import logger

CATEGORIES_QTY = 5
PRODUCTS_QTY = 40


class Command(BaseCommand):

    def handle(self, *args, **options):
        # create categories
        Category.objects.all().delete()
        for category in range(CATEGORIES_QTY):
            new_category = CategoryFactory()
            logger.info(f'{new_category.name} is created')

        # create products
        Product.objects.all().delete()
        for product in range(PRODUCTS_QTY):
            new_product = ProductFactory()
            logger.info(f'{new_product.name} is created')
