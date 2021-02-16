from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.db import models
from .models import Product, Tags, Category, Subscriber


class FlatPageCustom(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'price', 'title')


class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('id', 'subscriber')


admin.site.register(Product, ProductAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
