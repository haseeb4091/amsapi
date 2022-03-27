from django.db import models
class buildings(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
class Owner(models.Model):
    name = models.CharField(max_length=100)
class Room(models.Model):
    name = models.CharField(max_length=100)
    building =  models.CharField(max_length=100)
class addroom(models.Model):
    name = models.CharField(max_length=100)
    building =  models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
class customeraccount(models.Model):
    name = models.CharField(max_length=100)
    cnic = models.CharField(max_length=100)
    phno = models.IntegerField()
    role = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    rent = models.IntegerField()
    security = models.IntegerField()
    accountno = models.IntegerField()
    debt = models.IntegerField()
class allbills(models.Model):
    date = models.CharField(max_length=100)
    accountno = models.IntegerField()
    rent = models.IntegerField()
    security = models.IntegerField()
    bill = models.IntegerField()
    remaining = models.IntegerField()
    total = models.IntegerField()
    paid = models.IntegerField()



