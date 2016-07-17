
from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer

# Create your models here.
class Material(models.Model):
	customer = models.ForeignKey(Customer)
	material_name = models.CharField(max_length = 128)
	material_code = models.CharField(max_length = 20)
	control_code = models.CharField(max_length = 20)
	Pallet_unit = models.IntegerField(default = 1)
	Box_unit = models.IntegerField(default = 1)
	unit = models.CharField(max_length = 10, default = 'BOX')
	memo = models.TextField(blank = True)
	
	def __str__(self):
		return '{} ( {} [{}] )'.format(self.customer.customer_name,self.material_name,self.material_code)

class Zone(models.Model):
	zone = models.CharField(max_length = 20)

	def __str__(self):
		return self.zone

class Pallet(models.Model):
	pallet = models.CharField(max_length = 20)
	zone = models.ForeignKey(Zone)

	def __str__(self):
		return self.pallet

class Unit(models.Model):
	unit_code = models.CharField(max_length = 10)
	
	def __str__(self):
		return self.unit_code

class Packing(models.Model):
	Packing_code = models.CharField(max_length = 10)
	
	def __str__(self):
		return self.Packing_code

class Incoming(models.Model):
	pallet = models.ForeignKey(Pallet)
	material = models.ForeignKey(Material)
	incoming_date = models.DateTimeField('date incoming')
	incoming_unit = models.ForeignKey(Unit)
	incoming_count = models.IntegerField(default = 0)
	unpackBox_count = models.IntegerField(default = 0)

	def __str__(self):
		return '{} {} {}'.format(self.incoming_date, self.pallet, self.material)

class Outgoing(models.Model):
	pallet = models.ForeignKey(Pallet)
	material = models.ForeignKey(Material)
	outgoing_date = models.DateTimeField('date outgoing')
	outgoing_unit = models.ForeignKey(Unit)
	packing = models.ForeignKey(Packing)
	outgoing_count = models.IntegerField(default = 0)
	unpackBox_count = models.IntegerField(default = 0)
	
	def __str__(self):
		return '{} {}'.format(self.outgoing_date, self.material)