from django.shortcuts import render
from django.views.generic import TemplateView
from cart.cart import Cart
from catalog.models import Product, Category

PRODUCTS_QTY_IN_PREVIEW = 4


def split_list_by_limit(items_list, limit):
    return items_list[:limit] if len(items_list) > limit else items_list


class BaseView(TemplateView):
    template_name = 'shop/index.html'

    categories = Category.objects.all()
    preview_products = {}
    for category in categories:
        products_in_category = [product for product in Product.objects.filter(category=category)]
        preview_products[category] = split_list_by_limit(products_in_category, PRODUCTS_QTY_IN_PREVIEW)

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['categories'] = self.categories
            context['preview_products_in_category'] = self.preview_products
            return context

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        context = self.get_context_data(**kwargs)
        context['cart'] = cart

        return render(request, self.template_name, context)
