from django.db import models
from django.contrib.auth.models import User

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255)
    experience = models.TextField()

    def __str__(self):
        return self.name

class PerformerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255)
    experience = models.TextField()

    def __str__(self):
        return self.name
