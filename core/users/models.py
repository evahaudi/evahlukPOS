from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.dispatch import receiver

class Users(AbstractUser):
    is_chef = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_waiter = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    role = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)  
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Chef(models.Model):
    user = models.OneToOneField(Users, related_name="chef", on_delete=models.CASCADE)
    cuisine_specialty = models.CharField(max_length=50)
    experience_years = models.IntegerField()
    
    def __str__(self):
        return self.user.username

class Manager(models.Model):
    user = models.OneToOneField(Users, related_name="manager", on_delete=models.CASCADE)
    department = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username

class Waiter(models.Model):
    user = models.OneToOneField(Users, related_name="waiter", on_delete=models.CASCADE)
    assigned_tables = models.ManyToManyField('Table')
    
    def __str__(self):
        return self.user.username

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    
    def __str__(self):
        return f"Table {self.table_number}"

class Order(models.Model):
    waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE)
    items = models.ManyToManyField('MenuItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order by {self.waiter.user.username}"

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.name
