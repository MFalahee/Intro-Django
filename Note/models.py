from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    #user edited fields
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)

    #timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class PersonalNote(Note): #this new class inherits Note (and all of its fields)
    user = models.ForeignKey(User, on_delete=models.CASCADE) #FK to User