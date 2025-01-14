from django.urls import path
from order.views import *

urlpatterns = [
    path('create/', create_order, name='create_order'),
    path('success/', order_success, name='order_success'),
    path('all_orders/', all_orders, name='all_orders'),
    path('my-orders/', user_orders, name='user_orders'),
]
