from django.urls import path
from .views import (
    login,
    home,
    likes,
    notifications,
    orders,
    register,
    fines,
    logout

)
urlpatterns = [
    path('login/', login, name='login'),
    path('', home, name='home'),
    path('likes/', likes, name='likes'),
    path('notifications', notifications, name='notifications'),
    path('orders', orders, name='orders'),
    path('register/', register, name='register'),
    path('fines/', fines, name='fines'),
    path('logout/', logout, name='logout')

]