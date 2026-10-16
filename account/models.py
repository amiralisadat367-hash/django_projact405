from django.db import models

# Create your models here.

class Account(models.Model):
    name = models.CharField()
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} {self.age}"