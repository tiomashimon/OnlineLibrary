from django.contrib import admin
from .models import (
    Order, 
    OrderStatus
)

admin.site.register(Order)
admin.site.register(OrderStatus)