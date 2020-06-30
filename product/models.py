from django.db import models

class AllDoc(models.Model):
    name_ID = models.CharField(max_length = 100)
    name_Product = models.CharField(max_length = 100)
    name_price = models.CharField(max_length = 200)
    photo1 = models.ImageField(upload_to="gallery",blank=True,null=True)
    photo2 = models.ImageField(upload_to="gallery",blank=True,null=True)
    photo3 = models.ImageField(upload_to="gallery",blank=True,null=True)
  
    def __str__(self):
        return self.name_Product

class Allcustomer(models.Model):
	cutomer_id = models.CharField(max_length=100)
	tax_id =  models.CharField(max_length=100)
	company = models.TextField(null=True, blank=True)
	department= models.CharField(max_length=200,null=True, blank=True)
	cutomer_address = models.TextField(null=True, blank=True)
	customer_type = models.CharField(max_length=100,null=True, blank=True)

	