from django.db import models


class Person(models.Model):
    id = models.IntegerField(primary_key='true')
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    emailid = models.CharField(max_length=30)
    phone = models.IntegerField()
    PRN = models.CharField(max_length=15)

class Trainlist(models.Model):
    tid = models.CharField(primary_key='true', max_length=10)
    tname = models.CharField(max_length=100)

class rates(models.Model):
    city=models.CharField(primary_key='true', max_length=15)
    Ahmedabad = models.CharField(max_length=15)
    Nadiad = models.CharField(max_length=15)
    Anand = models.CharField(max_length=15)
    Vadodara = models.CharField(max_length=15)
    Bharuch = models.CharField(max_length=15)
    Surat = models.CharField(max_length=15)
    Navsari = models.CharField(max_length=15)
    Valsad = models.CharField(max_length=15)

class ticketdetails(models.Model):
    tnm=models.CharField(max_length=20)
    dt=models.CharField(max_length=10)
    cost = models.CharField(max_length=5)
    src=models.CharField(max_length=15)
    dest = models.CharField(max_length=15)
    num=models.CharField(max_length=1)
    mail=models.CharField(max_length=40)


class cost(models.Model):
    station_id=models.AutoField(primary_key='true')
    station=models.CharField(max_length=15)
    costy=models.CharField(max_length=10)
   



