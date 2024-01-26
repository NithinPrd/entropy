from django.contrib import admin

from blockchain.models import Block

# Register your models here.
@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', )