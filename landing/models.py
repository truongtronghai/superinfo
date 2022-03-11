from django.db import models

# Create your models here.


class Option(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=255, default="notitle")
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.title
