from django.db import models
from django.utils.translation import gettext_lazy as _
from core.apps.books.models import Book
from core.apps.users.models import User

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
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, verbose_name=_('Status'), related_name='orders')
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    booked_until = models.DateTimeField(_('Booked Until'), null=True, blank=True)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f'{self.user.username} - {self.book.title} - {self.status.name}'
