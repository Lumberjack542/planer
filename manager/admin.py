from django.contrib import admin
from .models import Product, Comments, Marks


# Register your models here.


class CommentsAdmin(admin.StackedInline):
    model = Comments
    extra = 0


class MarksAdmin(admin.StackedInline):
    model = Marks
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [CommentsAdmin, MarksAdmin]


admin.site.register(Product, ProductAdmin)
