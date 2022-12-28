from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
    
   
class ProductImage(models.Model):
    image = models.FileField('Arquivos',upload_to='image')
    product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
 
    def __str__(self):
        return self.product.name