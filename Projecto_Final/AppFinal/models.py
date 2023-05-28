from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=900)
    content = models.CharField(max_length=10000)
    category = models.CharField(max_length=45)
