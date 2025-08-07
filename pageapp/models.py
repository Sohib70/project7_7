from django.db import models

# Create your models here.

class Category(models.Model):
    nomi = models.CharField(max_length=100)

    def __str__(self):
        return self.nomi

class Sumka(models.Model):
    firmasi = models.CharField(max_length=50)
    rangi = models.CharField(max_length=50)
    materiali = models.CharField(max_length=50)
    davlati = models.CharField(max_length=50)
    price = models.PositiveIntegerField(blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.firmasi