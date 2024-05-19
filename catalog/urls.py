from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import products_list, product_details

app_name = CatalogConfig.name

urlpatterns = [
    path('', products_list, name='products_list'),
    path('products/<int:pk>/', product_details, name='product_details')
]
