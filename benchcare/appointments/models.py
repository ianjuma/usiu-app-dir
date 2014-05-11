from django.db import models


class Appointments(models.Model):
	surname = models.CharField(max_length=200)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	email_address = models.EmailField(max_length=75)
	phone_number = models.IntegerField()
	appointmnet_reason = models.TextField(max_length=1000)
	appointment_date = models.DateTimeField(auto_now_add=True)
	


	def __unicode__(self):
		return self.appointmnet_reason

