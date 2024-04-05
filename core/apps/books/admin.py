from django.contrib import admin
from .models import (
    Book,
    BookGenre,
    BookStatus,
    BookType
)


admin.site.register(Book)
admin.site.register(BookType)
admin.site.register(BookStatus)
admin.site.register(BookGenre)