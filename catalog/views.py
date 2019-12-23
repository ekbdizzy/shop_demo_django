from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from catalog.models import Category, Product
from cart.cart import Cart


class ProductsInCategoryView(View):
    template_name = 'catalog/products_in_category.html'

    def get(self, request, category_slug, *args, **kwargs):
        cart = Cart(request)
        categories = Category.objects.all()
        category = get_object_or_404(Category, slug=category_slug)
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
        product = get_object_or_404(Product, slug=product_slug)

        context = {
            'categories': categories,
            'product': product,
            'cart': cart,
        }

        return render(request, self.template_name, context)


def page_does_not_exists(request, exception):
    template_name = 'catalog/page_does_not_exists.html'
    return render(request, template_name, {})


def server_error(request):
    template_name = 'catalog/server_error.html'
    return render(request, template_name, {})
