from django.db import models

class AllCustomer(models.Model):
	customer_id = models.CharField(max_length=100,null=True, blank=True)
	tax_id =  models.CharField(max_length=100,null=True, blank=True)
	company = models.TextField(null=True, blank=True)
	department= models.CharField(max_length=200,null=True, blank=True)
	customer_address = models.TextField(null=True, blank=True)
	customer_type = models.CharField(max_length=100,null=True, blank=True)
	def __str__(self):
		return self.company

class Image(models.Model):
	image1 = models.ImageField(upload_to='media',null=True, blank=True)
	def __str__(self):
		return self.image1
