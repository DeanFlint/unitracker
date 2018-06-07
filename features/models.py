from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

""" This is where we will specify the models in our db """

class Feature(models.Model):
    STATUS_CHOICES = ( 
        ('todo', 'To Do'),
        ('inprogress', 'In Progress'),
        ('done', 'Done')
    )
    
    name = models.CharField(max_length=75)
    desc = models.TextField(max_length=500)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="todo")

    def __str__(self):
        return self.name

class FeatureComment(models.Model):
    feature = models.ForeignKey(Feature, null=True)
    user = models.ForeignKey(User, null=True)
    comment = models.TextField(max_length=500)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    def __str__(self):
        return self.comment
        

class FeatureUserVotes(models.Model):
    featuree = models.ForeignKey(Feature)
    user = models.ForeignKey(User, null=True)