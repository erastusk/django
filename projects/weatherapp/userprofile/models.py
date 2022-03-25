from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile_cities(models.Model):
    city = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.city


