from django.contrib import admin
from .models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'comfort', 'capacity', 'price', 'created_date')
    list_filter = ('comfort',)
    search_fields = ('title', 'text')
