from django.contrib import admin
from .models import Chef, Manager, MenuItem, Waiter, Table, Order
# Register your models here.

admin.site.register(Chef)
admin.site.register(Manager)
admin.site.register(MenuItem)
admin.site.register(Waiter)
admin.site.register(Table)
admin.site.register(Order)


