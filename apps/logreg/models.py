from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	birthdate = models.CharField(max_length=50)
	class Meta:
		db_table ='users'


