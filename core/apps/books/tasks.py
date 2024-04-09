from core.project.celery import app
from core.apps.orders.models import (
    OrderStatus,
    Order,
)
from .models import Fine
from datetime import datetime
from core.apps.users.tasks import send_email_to_user
from django.conf import settings

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
                
            book_title = order.book.title
            book_author = order.book.author  
            from_email = settings.EMAIL_HOST_USER
            send_email_to_user.delay(
                from_email=from_email,
                recipient_list=[order.user.email],
                subject="Fine Notification - OnlineLibrary", 
                message=f"Hello {order.user.username},\n\nThis is to inform you that you have been fined for the overdue book '{book_title}' by {book_author}.\n\nFine Amount: {days_passed * 10} UAH\n\nIf you have any questions or concerns regarding this fine, please contact us at {from_email}.\n\nThank you for your attention.\n\nBest regards,\nOnlineLibrary"
            )