from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.email


class Details(models.Model):
    name=models.CharField(max_length=255)
    image = models.ImageField(upload_to='media',null=True,blank=True)
    description = models.TextField()
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


