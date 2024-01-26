from django.db import models
from django.core.validators import RegexValidator

class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    region = models.CharField(max_length=10)
    current_party = models.CharField(max_length=20)