from django.db import models
from django.urls import reverse

# Create your models here.
# Entity (Inherit Model)
# default CRUD including (all, create)
# Product.objectsa.all()
class Product(models.Model):
    title = models.CharField(max_length=120) #max_length=120
    desc = models.TextField(blank=True, null=True)
    email = models.EmailField(null=False)
    price = models.DecimalField(max_digits=5, decimal_places=3)
    summary = models.TextField(blank=True, null=False) # default = default value 
    # blank is deal with the view, null is deal with the database
    feature = models.BooleanField(default=False) # null=True # default=True

    def get_abs_url(self):
        ## kwrgs = keyword arguments that is going pass in the url (e.g. <int:my_id>)
        return reverse("product-detail-id", kwargs={"my_id": self.id}) #f"/product_detail/{self.id}"