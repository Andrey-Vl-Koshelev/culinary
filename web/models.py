from django.db import models

class Web(models.Model):
    image = models.ImageField(upload_to='web/images/',null=True, blank=True)


class Blog(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.name == None:
            return 'Пользователь'
        return self.name
