from django.contrib import admin
from .models import (
    Book,
    BookGenre,
    BookStatus,
    BookType,
    Fine,
    Like
)


admin.site.register(Book)
admin.site.register(BookType)
admin.site.register(BookStatus)
admin.site.register(BookGenre)
admin.site.register(Fine)
admin.site.register(Like)
