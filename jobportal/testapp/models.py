from django.db import models

# Create your models here.
class hydjobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    title=models.CharField(max_length=20);
    eligibility=models.CharField(max_length=50);
    address=models.CharField(max_length=100);
    email=models.EmailField();
    phonenumber=models.IntegerField(max_length=10)


class bengjobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    title=models.CharField(max_length=20);
    eligibility=models.CharField(max_length=50);
    address=models.CharField(max_length=100);
    email=models.EmailField();
    phonenumber=models.IntegerField(max_length=10)

class chenjobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    title=models.CharField(max_length=20);
    eligibility=models.CharField(max_length=50);
    address=models.CharField(max_length=100);
    email=models.EmailField();
    phonenumber=models.IntegerField(max_length=10)

class punejobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    title=models.CharField(max_length=20);
    eligibility=models.CharField(max_length=50);
    address=models.CharField(max_length=100);
    email=models.EmailField();
    phonenumber=models.IntegerField(max_length=10)

class mumjobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    title=models.CharField(max_length=20);
    eligibility=models.CharField(max_length=50);
    address=models.CharField(max_length=100);
    email=models.EmailField();
    phonenumber=models.IntegerField(max_length=10)
