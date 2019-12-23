from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category

    prepopulated_fields = {"slug": ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_active', 'price')
    list_filter = ('category', 'is_active')
    prepopulated_fields = {"slug": ('name',)}
    search_fields = ('name',)

    class Meta:
        model = Product
        ordering = ('name',)
