from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = models.CharField(_('Username'), max_length=100, unique=True)
    email = models.CharField(_('Email'), max_length=255)
    phone = PhoneNumberField(_('Phone'), null=False, blank=False, unique=True)
    image = models.ImageField(_('Image'), upload_to='users/%Y/%m/%d/', blank=True)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


class UserCharacteristics(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sales_count = models.IntegerField(default=0)
    borrowing_count = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=4)

    def __str__(self):
        return f'{self.user.username} - Sales: {self.sales_count}, Borrowings: {self.borrowing_count}, Rating: {self.rating}'
