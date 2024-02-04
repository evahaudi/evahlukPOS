from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.dispatch import receiver

class Users(AbstractUser):

    CHEF = 'Chef'
    MANAGER = 'Manager'
    WAITER = 'Waiter'

    ROLE_CHOICES = [
        (CHEF, 'Chef'),
        (MANAGER, 'Manager'),
        (WAITER, 'Waiter'),
    ]
    is_chef = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_waiter = models.BooleanField(default=False)
    birthdate = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, null=True, blank=True)
    experienceyears = models.IntegerField(null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    fullname = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)  
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Chef(models.Model):
    user = models.OneToOneField(Users, related_name="chef", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Manager(models.Model):
    user = models.OneToOneField(Users, related_name="manager", on_delete=models.CASCADE)
  
    
    def __str__(self):
        return self.user.username

class Waiter(models.Model):
    user = models.OneToOneField(Users, related_name="waiter", on_delete=models.CASCADE)
    assigned_tables = models.ManyToManyField('Table')
    
    def __str__(self):
        return self.user.username

class Table(models.Model):
    table_number = models.IntegerField(unique=True, null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"Table {self.table_number}"

class Order(models.Model):
    waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE)
    items = models.ManyToManyField('MenuItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return f"Order by {self.waiter.user.username}"

class MenuItem(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return self.name
