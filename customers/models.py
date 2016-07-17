from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
	user = models.OneToOneField(User)
	customer_name = models.CharField(max_length = 60)
	manager = models.CharField(max_length = 12, blank = True)
	telephone_1 = models.CharField(max_length = 20, blank = True)
	telephone_2 = models.CharField(max_length = 20, blank = True)
	fax = models.CharField(max_length = 20, blank = True)
	cellurphone = models.CharField(max_length = 20,blank = True)
	email = models.EmailField(max_length = 128, blank = True)
	address = models.CharField(max_length = 128, blank = True)
	memo = models.TextField(blank = True)
	# agency = models.ManyToManyField(User, related_name='agency_set')

	def __str__(self):
		return '{}'.format(self.customer_name,)

class Agency(models.Model):
	user = models.OneToOneField(User)
	agency_name = models.CharField(max_length = 60)
	def __str__(self):
		return '{}'.format(self.agency_name,)
