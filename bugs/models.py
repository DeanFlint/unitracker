from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.utils import timezone

""" This is where we will specify the models in our db """

class Bug(models.Model):
    STATUS_CHOICES = ( 
        ('todo', 'To Do'),
        ('inprogress', 'In Progress'),
        ('done', 'Done')
    )
    
    name = models.CharField(max_length=75)
    desc = models.TextField(max_length=500)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="To Do")

    def __str__(self):
        return self.name

class Comment(models.Model):
    bug = models.ForeignKey(Bug, null=True)
    user = models.ForeignKey(User, null=True)
    comment = models.TextField(max_length=500)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    def __str__(self):
        return self.comment
        

class UserVotes(models.Model):
    bugg = models.ForeignKey(Bug, null=True)
    user = models.ForeignKey(User, null=True)