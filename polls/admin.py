from django.contrib import admin

from . import models
#from .models import Question <- what the tutorial site says to do
admin.site.register(models.Question)
# Register your models here.