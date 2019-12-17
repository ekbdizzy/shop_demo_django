from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, default='', blank=True)
    slug = models.SlugField(blank=True)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('catalog:products_in_category', kwargs={'category_slug': self.slug})

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):

    def image_folder(self, filename):
        filename = ".".join([self.slug, filename.split('.')[-1]])
        return f'products/{self.slug}/{filename}'

    name = models.CharField(max_length=100, default=None, blank=True)
    slug = models.SlugField(blank=True)
    description = models.TextField(max_length=2000, blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to=image_folder)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('catalog:product_detail', kwargs={'product_slug': self.slug})

    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
