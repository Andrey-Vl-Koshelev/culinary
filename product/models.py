from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField()
    image = models.ImageField(upload_to='web/images/')
    new_price = models.IntegerField(default=0, null=True, blank=True)
    old_price = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name
