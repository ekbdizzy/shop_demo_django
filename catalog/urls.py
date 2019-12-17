from django.conf import settings
from django.urls import path
from .views import ProductsInCategoryView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('category/<category_slug>', ProductsInCategoryView.as_view(), name='products_in_category'),
    path('product/<product_slug>', ProductDetailView.as_view(), name='product_detail'),
]
