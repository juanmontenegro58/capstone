from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import *


urlpatterns = [
    path('message/', msg),
    path('menu-items/', MenuItemsView.as_view()),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]