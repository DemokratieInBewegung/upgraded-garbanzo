from django.contrib.auth.models import User
from datetime import datetime, timedelta, date
from django.db import models
import pytz

class InviteBatch(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
	total_found = models.IntegerField(default=0)
	new_added = models.IntegerField(default=0)
	payload = models.TextField()