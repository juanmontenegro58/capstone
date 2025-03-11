from django.urls import path

from .views import *

urlpatterns = [
    # path('', sayHello, name = 'sayHello'),
    path('', index, name = 'index')
]