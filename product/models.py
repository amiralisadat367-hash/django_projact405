from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=256)
    dis = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    is_active = models.BooleanField()
    count = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
