# models.py
from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20)
    ages=models.CharField(max_length=20,default="")

class emo_test(models.Model):
    goodsId = models.CharField(max_length=20,default="")
    productTitle=models.CharField(max_length=512,default="")
    storeId=models.CharField(max_length=32,default="")
    storeName=models.CharField(max_length=128,default="")
    new=models.CharField(max_length=128,default="")

class popular_type(models.Model):
    type =models.CharField(max_length=20,default="")
    freq =models.CharField(max_length=20,default="")
class price_amount(models.Model):
    price = models.CharField(max_length=20, default="")
    amount = models.CharField(max_length=20, default="")


class shop1(models.Model):
    productTitle = models.CharField(max_length=512, default="")
    productStatus = models.CharField(max_length=20, default="")

class shop2(models.Model):
    productTitle = models.CharField(max_length=512, default="")
    productStatus = models.CharField(max_length=20, default="")

class shop3(models.Model):
    productTitle = models.CharField(max_length=512, default="")
    productStatus = models.CharField(max_length=20, default="")

class shop4(models.Model):
    productTitle = models.CharField(max_length=512, default="")
    productStatus = models.CharField(max_length=20, default="")

class shop5(models.Model):
    productTitle = models.CharField(max_length=512, default="")
    productStatus = models.CharField(max_length=20, default="")

class shop6(models.Model):
    productTitle = models.CharField(max_length=512, default="")
    productStatus = models.CharField(max_length=20, default="")

class shop7(models.Model):
    productTitle = models.CharField(max_length=512, default="")
    productStatus = models.CharField(max_length=20, default="")
class shop8(models.Model):
    productTitle = models.CharField(max_length=512, default="")
    productStatus = models.CharField(max_length=20, default="")
class shop9(models.Model):
    productTitle = models.CharField(max_length=512, default="")
    productStatus = models.CharField(max_length=20, default="")

