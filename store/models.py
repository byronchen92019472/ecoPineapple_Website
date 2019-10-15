from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


#Products
class Product(models.Model):

    PRODUCT_CATEGORY = (('Cleaning', 'Cleaning'),
        ('Furniture','Furniture'),
        ('Personal', 'Personal'),
        ('Food & Drink', 'Food & Drink'))

    #product_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
    #help_text="Unique ID for this Product")
    category = models.CharField(choices=PRODUCT_CATEGORY, max_length=30)
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    desc_short = models.CharField(max_length=200)
    desc_long = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    image = models.ImageField(upload_to='images')
    hero = models.BooleanField()





    def __str__(self):
        #String for representing the Model object
        return '{0} ({1})'.format(self.id,self.name)



    #https://blog.khophi.co/extending-django-user-model-userprofile-like-a-pro/


#Rockets
class Rocket(models.Model):

    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    desc_short = models.CharField(max_length=200)
    desc_long = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    image = models.ImageField(upload_to='images')
    hero = models.BooleanField()





    def __str__(self):
        #String for representing the Model object
        return '{0} ({1})'.format(self.id,self.name)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=30, blank=True)


    PROFILE_DEPARTMENT = (('Management', 'Management'),
        ('Sales','Sales'),
        ('Marketing','Marketing'),
        ('Information Technology', 'Information Technology'),
        ('Operations', 'Operations'),
        ('Finance', 'Finance'),
        ('Legal', 'Legal'),
        ('Human Resources', 'Human Resources'))
    department = models.CharField(choices=PROFILE_DEPARTMENT, max_length=30, blank=True)


    
    def __str__(self):
        #String for representing the Model object
        return '{0} ({1})'.format(self.id,self.user)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()





class Category(models.Model):

    
    #product_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
    #help_text="Unique ID for this Product")
    name = models.CharField(max_length=30)

    def __str__(self):
        #String for representing the Model object (in Admin site etc.)
        return self.name
    