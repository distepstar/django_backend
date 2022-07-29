from django.contrib import admin

# relative import 
# from "py file name" import "Class"
from .models import Product

admin.site.register(Product)
