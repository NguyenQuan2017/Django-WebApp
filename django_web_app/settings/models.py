from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import os

class Setting(models.Model):
    viettel_key = models.CharField(max_length=200)
    fpt_key = models.CharField(max_length=200)
    rss_key = models.CharField(max_length=200)
    tssfree_key = models.CharField(max_length=200)
    signature = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)



