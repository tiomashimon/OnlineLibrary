from django.contrib import admin
from .models import (
    User,
    UserCharacteristics
)

admin.site.register(User)
admin.site.register(UserCharacteristics)