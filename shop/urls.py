from django.urls import path
from .views import BaseView

app_name = 'shop'

urlpatterns = [
    path('', BaseView.as_view(), name='base')
]
