from django.shortcuts import render
from django.views.generic import TemplateView
from cart.cart import Cart
from catalog.models import Product, Category
import logging


# Create your views here.
class BaseView(TemplateView):
    template_name = 'shop/index.html'

    categories = Category.objects.all()
    preview_products_in_category = {}
    for category in categories:
        products_in_category = Product.objects.filter(category=category)
        if len(products_in_category) > 4:
            preview_products_in_category[category] = [product for product in products_in_category[:4]]
        else:
            preview_products_in_category[category] = [product for product in products_in_category]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.categories
        context['preview_products_in_category'] = self.preview_products_in_category
        return context

    def get(self, request, *args, **kwargs):

        cart = Cart(request)
        context = self.get_context_data(**kwargs)
        context['cart'] = cart

        return render(request, self.template_name, context)
