from django.db import models
from pyuploadcare.dj.models import ImageField
import datetime as dt


class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published_status = models.BooleanField(default=False)
    content = models.TextField(max_length=500,blank=False, default='')
    modified_date = models.DateTimeField(auto_now=True)
    photo = ImageField(manual_crop='1280x720',blank=True)
   
    
