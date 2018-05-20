from django.contrib import admin
from .models import Bug, Comment

# Register your models here.
admin.site.register(Bug)
admin.site.register(Comment)