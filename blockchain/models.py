from hashlib import sha256
import json
from django.db import models
from django.forms import model_to_dict

# Create your models here.
class Block(models.Model):
    id = models.AutoField(primary_key=True)
    hash = models.CharField(max_length=200, editable=False)
    data = models.JSONField()
    timestamp = models.DateTimeField()
    previous_hash = models.CharField(max_length=50, default='0', editable=False)

    def save(self, *args, **kwargs):
        print(self.__dict__)
        latest_block = Block.objects.last()
        if latest_block is not None:
            for item in latest_block.values():
                self.previous_hash = item['hash']
        block_string = json.dumps(model_to_dict(self), sort_keys=True, default=str)
        self.hash = sha256(block_string.encode()).hexdigest()
        super().save(*args, **kwargs)
