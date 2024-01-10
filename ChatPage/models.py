from django.db import models
from django.utils import timezone

# Create your models here.
class ChatHistory(models.Model):
    sendUser = models.CharField(max_length=128)
    sendMessage = models.TextField()
    sendRoom = models.CharField(max_length=256)
    sendAt = models.DateTimeField(default=timezone.now)