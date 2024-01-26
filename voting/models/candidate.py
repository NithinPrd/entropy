from django.db import models
from django.core.validators import RegexValidator

from voting.models.state import State

class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 11 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=13, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)