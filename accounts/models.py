from django.db import models

# Create your models here.


class iconPath(models.Model):
    userid = models.CharField(max_length=128)
    filepath = models.ImageField(upload_to="images/icons/")
