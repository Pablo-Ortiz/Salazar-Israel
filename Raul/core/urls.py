from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('form', Form, name="form-cliente"),
    path('list/<str:username>', List, name="list"),
    path('profile/<str:username>', profile, name='profile'),
]