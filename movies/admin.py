from django.contrib import admin

from .models import Director, Movie, Category, Order


# Register your models here.
admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Order)
