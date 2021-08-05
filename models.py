from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.EmailField(max_length=196)
    subject = models.CharField(max_length=196)
    message = models.TextField()

    def __str__(self):
        return self.email

class Register(models.Model):
    firstname = models.CharField(max_length=196)
    lastname = models.CharField(max_length=196)
    email = models.EmailField(max_length=196)
    gender = models.CharField(max_length=196, default='')

    def __str__(self):
        return self.firstname

class Male(models.Model):
    age = models.CharField(max_length=196)

    def __str__(self):
        return self.age

class Female(models.Model):
    age = models.CharField(max_length=196)

    def __str__(self):
        return self.age