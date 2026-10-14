from django.db import models

# Create your models here.
class Accont(models.Model):
    email =models.EmailField(unique=True)
    user_id = models.CharField(max_length=150,unique=True,blank=True)
    name = models.CharField(max_length=125)
    password = models.CharField(max_length=256)
    coin = models.IntegerField(default=0)
    img = models.ImageField(upload_to="profile/")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        if not self.user_id:
            self.user_id = self.email.split('@')[0]
        super().save(*args,**kwargs)