from django.db import models
from  django.utils import timezone
from django.contrib.auth.models import AbstractUser

# class DateHolder(models.Model):
#     created_at=models.DateField(auto_now_add=True)
#     updated_at=models.DateField(auto_now=True)

#     class Meta:
#         abstract = True


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='user_pics',null=True,blank=True,default="default.png")
    birthday = models.DateField(null=True,blank=True)
    
    def __str__(self):
        return self.username
    



class TODO(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    important = models.IntegerField(default=0)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'

    