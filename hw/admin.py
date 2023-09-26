from django.contrib import admin

from hw.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('title', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product_ref', 'number', 'name', 'is_current',)
    list_filter = ('product_ref', 'is_current',)
