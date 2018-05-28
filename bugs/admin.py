from django.contrib import admin
from .models import Bug, BugComment, BugUserVotes

# Register your models here.
admin.site.register(Bug)
admin.site.register(BugComment)
admin.site.register(BugUserVotes)