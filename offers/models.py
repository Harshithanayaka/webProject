from django.db import models

class plans(models.Model):
    id=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=20)
    pprize=models.IntegerField()

class postpaid(models.Model):
    id=models.IntegerField(primary_key=True)
    pstname=models.CharField(max_length=20)
    pstprize=models.IntegerField()

class dongle(models.Model):
    id=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=20)
    dprize=models.IntegerField()

class userdetails(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    mobile=models.IntegerField()
    def __str__(self):
        return self.title

class Customer(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    address=models.CharField(max_length=30)
    aadhar=models.CharField(max_length=50)
    def __str__(self):
        return self.title

class newconnection(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.CharField(max_length=20)
    aadhar=models.IntegerField()
    def __str__(self):
        return self.title

class invoice(models.Model):
    invoice_id=models.IntegerField()
    name=models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    plan_name=models.CharField(max_length=20)
    month = models.IntegerField()
    mobile = models.IntegerField()

# Create your models here.
