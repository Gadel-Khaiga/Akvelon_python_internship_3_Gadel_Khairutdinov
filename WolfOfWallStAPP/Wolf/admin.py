from django.contrib import admin
from .models import  Wolf

# Register your models here.

class WolfAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('id', 'first_name', 'last_name', 'email')
    list_editable = ('first_name', 'last_name', 'email')