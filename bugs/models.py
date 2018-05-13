from django.db import models

""" This is where we will specify the models in our db """

class Bug(models.Model):
    name = models.CharField(max_length=75)
    desc = models.TextField(max_length=500)
    status = models.CharField(max_length=15, default="To Do")
    votes = models.IntegerField(null=False, default=0)
    
    def __str__(self):
        return self.name
