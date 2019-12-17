from django.shortcuts import render
from django.views import View
from catalog.models import Category, Product
from cart.cart import Cart


# Create your views here.
class ProductsInCategoryView(View):
    template_name = 'catalog/products_in_category.html'

    def get(self, request, category_slug, *args, **kwargs):
        cart = Cart(request)
        categories = Category.objects.all()
        category = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(category=category)
        context = {
            'categories': categories,
            'category': category,
            'products': products,
            'cart': cart,
        }
        return render(request, self.template_name, context)


class ProductDetailView(View):
    template_name = 'catalog/product_detail.html'

    def get(self, request, product_slug, *args, **kwargs):
        cart = Cart(request)
        categories = Category.objects.all()
        product = Product.objects.get(slug=product_slug)

        context = {
            'categories': categories,
            'product': product,
            'cart': cart,
        }

        return render(request, self.template_name, context)
