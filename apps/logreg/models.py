from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	birthdate = models.CharField(max_length=100)
	class Meta:
		db_table ='users'


