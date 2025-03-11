from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    ...

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    ...