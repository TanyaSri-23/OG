from django.db import models
from datetime import datetime

class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length = 122)
    desc=models.TextField()
    date= models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return self.name