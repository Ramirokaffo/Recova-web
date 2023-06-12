from django.contrib import admin
from .models import Products


# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ("name", "description", "price", "slug", "actif")


admin.site.register(Products, AdminProduct)


"""
python3 manage.py shell    
"""