from django.contrib import admin

from blockchain.models import Block
from voting.models.candidate import Candidate
from voting.models.state import State

# Register your models here.
@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'state')

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'current_party')