from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAuthenticated
)

from .models import *
from .serializers import *

# Create your views here.
def sayHello(request):
    return HttpResponse('Hello Word')

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(ListCreateAPIView):

    queryset = Menu.objects.all()
    http_method_names = ['get', 'post']
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):

    queryset = Menu.objects.all()
    http_method_names = ['get', 'put', 'delete']
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]