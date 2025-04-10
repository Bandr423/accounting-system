from django.urls import path
from .views import inventory_list, sales_list, add_sale, purchases_list, add_purchase

urlpatterns = [
    path('inventory/', inventory_list, name='inventory_list'),
    path('sales/', sales_list, name='sales_list'),
    path('sales/add/', add_sale, name='add_sale'),
    path('purchases/', purchases_list, name='purchases_list'),
    path('purchases/add/', add_purchase, name='add_purchase'),
]