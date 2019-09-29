from django.db import models
import uuid

# Create your models here.


#Products
class Product(models.Model):

    PRODUCT_CATEGORY =(
        ('Cleaning', 'Cleaning'),
        ('Furniture','Furniture'),
        ('Personal', 'Personal'),
        ('Food & Drink', 'Food & Drink')
    )

    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this Product")
    category = models.CharField(choices=PRODUCT_CATEGORY, max_length=30)
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    desc_short = models.CharField(max_length=200)
    desc_long = models.CharField(max_length=1000)
    price=models.DecimalField(max_digits=16, decimal_places=2)
    image = models.ImageField(upload_to='images')




    def __str__(self):
        return self.brand + ' ' + self.name