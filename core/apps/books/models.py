from django.db import models
from django.utils.translation import gettext_lazy as _
from core.apps.users.models import User

class BookType(models.Model):
    name = models.CharField(_('Type'), max_length=100)

    class Meta:
        verbose_name = _("Book's type")
        verbose_name_plural = _("Book's types")

    def __str__(self):
        return self.name


class BookGenre(models.Model):
    name = models.CharField(_('Genre'), max_length=100)

    class Meta:
        verbose_name = _("Book's Genre")
        verbose_name_plural = _("Book's Genres")

    def __str__(self):
        return self.name


class BookStatus(models.Model):
    name = models.CharField(_('Status'), max_length=100)

    class Meta:
        verbose_name = _("Book's Status")
        verbose_name_plural = _("Book's Statuses")

    def __str__(self):
        return self.name


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books_owned')
    type = models.ForeignKey(BookType, on_delete=models.CASCADE, verbose_name=_('Type'), related_name='books')
    title = models.CharField(_('Title'), max_length=255)
    author = models.CharField(_('Author'), max_length=255)
    genre = models.ForeignKey(BookGenre, on_delete=models.CASCADE, verbose_name=_('Genre'), related_name='books')
    description = models.TextField(_('Description'), blank=True)
    publication_year = models.PositiveIntegerField(_('Publication Year'))
    image = models.ImageField(_('Image'), upload_to='books/%Y/%m/%d/', blank=True)
    available_copies = models.PositiveIntegerField(_('Available Copies'))
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    status = models.ForeignKey(BookStatus, on_delete=models.CASCADE, verbose_name=_('Status'), related_name='books')
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def __str__(self):
        return self.title


class Fine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fines', verbose_name=_('User'))
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='unpaid_fines', verbose_name=_('Book'))
    amount = models.IntegerField(_('Amount'))
    paid = models.BooleanField(_('Is user paid'), default=False)
    

    class Meta:
        verbose_name = _("Fine")
        verbose_name_plural = _("Fines")


    def __str__(self):
        return f'{self.amount}'