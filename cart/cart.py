from django.conf import settings
from django.http import Http404
from catalog.models import Product
import logging


class Cart(object):
    def __init__(self, request):
        if not request.session.get(settings.CART):
            request.session[settings.CART] = {}
        self.cart = request.session[settings.CART]

    def add_to_cart(self, product_id, quantity):

        if self.cart.get(product_id, None):
            self.cart[product_id]['quantity'] += quantity
        else:
            try:
                product = Product.objects.get(id=product_id)
                self.cart['product_id'] = {
                    'name': product.name,
                    'quantity': quantity,
                    'price': product.price,
                }
            except Product.DoesNotExist as error:
                logging.error(error)
                raise Http404

    def remove_from_cart(self, product_id):
        if self.cart.get(product_id, None):
            del self.cart[product_id]

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.cart.keys():
            if isinstance(product, int):
                total_quantity += self.cart[product]['quantity']
        return total_quantity

    def get_total_price(self):
        total_price = 0
        for product in self.cart.keys():
            if isinstance(product, int):
                total_price += self.cart[product]['quantity'] * self.cart[product]['price']
        return total_price
