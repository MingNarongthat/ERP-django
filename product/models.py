from django.db import models

class AllDoc(models.Model):
    name_ID = models.CharField(max_length = 100)
    name_Product = models.CharField(max_length = 100)
    name_price = models.CharField(max_length = 200)
    photo = models.ImageField(upload_to="gallery",blank=True,null=True)
  
    def __str__(self):
        return self.name_Product