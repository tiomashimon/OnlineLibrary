from django.db import models
from django.utils.translation import gettext_lazy as _
from core.apps.books.models import Book
from core.apps.users.models import User
from core.apps.users.tasks import send_email_to_user
from django.conf import settings

class OrderStatus(models.Model):
    name = models.CharField(_('Status'), max_length=255)

    class Meta:
        verbose_name = _("Order Status")
        verbose_name_plural = _("Order Statuses")

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name=_('User'))
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='orders', verbose_name=_('Book'))
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2, blank=True, default=0)
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True, verbose_name=_('Status'), related_name='orders')
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    booked_until = models.DateTimeField(_('Booked Until'), null=True, blank=True)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f'{self.user.username} - {self.book.title} - {self.status.name}'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._original_status = self.status

    def save(self, *args, **kwargs):
        if self.id:  
            if self.status != self._original_status:
                new_status = self.status
                user = self.user
                from_email = settings.EMAIL_HOST_USER

                subject = 'Change of Order Status'
                message = f"Dear {user.username},\n\nWe are writing to inform you that the status of your order has been updated.\n\nNew Order Status: {new_status}\n\nIf you have any questions or concerns regarding your order, please feel free to contact us.\n\nThank you for choosing our service.\n\nBest regards,\nOnlineLibrary"
                from_email = from_email
                recipient_list = [user.email,]

                send_email_to_user(subject, message, from_email, recipient_list)

        super().save(*args, **kwargs)
