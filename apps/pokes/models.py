from __future__ import unicode_literals

from django.db import models
from ..logreg.models import User

class Poke(models.Model):
	user_poked = models.ForeignKey(User, related_name='+')
	poked_by = models.ForeignKey(User, related_name='+')
	class Meta:
		db_table = 'pokes'

