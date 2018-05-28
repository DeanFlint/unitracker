from django.contrib import admin
from .models import Feature, FeatureComment, FeatureUserVotes

# Register your models here.
admin.site.register(Feature)
admin.site.register(FeatureComment)
admin.site.register(FeatureUserVotes)