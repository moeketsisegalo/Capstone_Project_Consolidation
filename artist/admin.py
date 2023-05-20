#import django modules
from django.contrib import admin
from django.contrib import admin
from .models import Album, Tour

# Register your models here.
admin.site.register(Album)
admin.site.register(Tour)
