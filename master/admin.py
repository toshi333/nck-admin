from django.contrib import admin
from .models import AppUser, Customer, Product


admin.site.register(AppUser)
admin.site.register(Customer)
admin.site.register(Product)