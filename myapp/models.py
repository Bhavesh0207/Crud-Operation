from django.db import models
from django. utils.safestring import mark_safe
# Create your models here.
GENDER = (
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE"),
    ("OTHER", "OTHER")
)
class product(models.Model):
    productname = models.CharField(max_length=40)
    productprice = models.FloatField()
    productdesc = models.TextField()
    productimage = models.ImageField(upload_to="photos")

    def product_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.productimage.url))

    product_photo.allow_tags = True

    def __str__(self):
        return self.productname


class login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=25)


class registration(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    gender = models.CharField(max_length=20)
    phone_number = models.BigIntegerField(null=True)
    address = models.TextField()
    role = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='photos')

    def product_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.profile_picture.url))

    product_photo.allow_tags = True

    def __str__(self):
        return self.name


class carttable(models.Model):
    userid = models.ForeignKey(registration, on_delete=models.CASCADE) # to know whose cart it is
    productid = models.ForeignKey(product, on_delete=models.CASCADE) # to know what product you have added
    quantity = models.FloatField() # to know what quantity you have selected
    totalamount = models.IntegerField() # total of base price and quantity
    cartstatus = models.IntegerField(null=True) # to know the status of cart -- 0 = delete, 1 = add, 2 = order placed
    orderid = models.IntegerField(null=True) # for future reference


class ordertable(models.Model):
    userid = models.ForeignKey(registration, on_delete=models.CASCADE)
    finaltotal = models.IntegerField()
    paymode = models.CharField(max_length=40)
    name =models.CharField(max_length=40) # name of receiver while delivery
    address =models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)