from django.shortcuts import render

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView
)
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework.decorators import (
    api_view,
    permission_classes
)

from .models import *
from .serializers import *

# Create your views here.
@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return 

class MenuItemsView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    http_method_names = ['get','post']
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    http_method_names = ['get', 'put', 'delete']