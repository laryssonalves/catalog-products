from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'visibility')


@admin.register(models.Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.Buyer)
class BuyersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'products')
