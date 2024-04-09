from core.project.celery import app
from core.apps.orders.models import (
    OrderStatus,
    Order,
)
from .models import Fine
from datetime import datetime

@app.task
def auto_assigning_fine():
    borrowed_status = OrderStatus.objects.get(name='Borrowed') 
    orders = Order.objects.filter(status=borrowed_status)

    for order in orders:
        booked_until_date = datetime.combine(order.booked_until, datetime.min.time()) 

        current_date = datetime.now()

        days_passed = (current_date - booked_until_date).days
        
        if days_passed >= 1:
                try:
                    fine = Fine.objects.get(user=order.user, book=order.book)
                    fine.amount = days_passed * 10
                    fine.save()
                except Fine.DoesNotExist:
                    Fine.objects.create(user=order.user, book=order.book, amount=days_passed * 10)