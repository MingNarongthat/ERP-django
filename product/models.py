from django.db import models

class AllCustomer(models.Model):
	cutomer_id = models.CharField(max_length=100,null=True, blank=True)
	tax_id =  models.CharField(max_length=100,null=True, blank=True)
	company = models.TextField(null=True, blank=True)
	department= models.CharField(max_length=200,null=True, blank=True)
	cutomer_address = models.TextField(null=True, blank=True)
	customer_type = models.CharField(max_length=100,null=True, blank=True)
	def __str__(self):
		return self.company
	