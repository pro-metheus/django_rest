from django.db import models

# Create your models here.
import uuid
from django.contrib.auth.models import User

class APIauth(models.Model):
    user=models.OneToOneField(User)
    api_key=models.CharField(max_length=36,default=uuid.uuid4().hex)
