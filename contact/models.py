from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    created_date = models.DateField(default = timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default = True)
    picture = models.ImageField(blank=True,upload_to ="pictures/%Y/%m/")
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True, null=True)
    owner =  models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True)
    def __str__(self):
        return self.first_name