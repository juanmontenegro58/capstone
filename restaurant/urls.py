from django.urls import (
    path,
    include
)
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'tables', BookingViewSet)

urlpatterns = [
    # path('', sayHello, name = 'sayHello'),
    path('', index, name = 'index'),

    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
]