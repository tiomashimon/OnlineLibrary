from django.contrib import admin
from .models import (
    User,
    UserCharacteristics,
    Notification,
    NotificationType
)

admin.site.register(User)
admin.site.register(UserCharacteristics)
admin.site.register(Notification)
admin.site.register(NotificationType)