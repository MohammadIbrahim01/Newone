# models.py
from django.db import models
from autoslug import AutoSlugField

class Sas(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

