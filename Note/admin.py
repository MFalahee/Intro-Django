from django.contrib import admin
from .models import Note

#this class is to get read-only fields to show up in the interface
class NoteAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register(Note, NoteAdmin)

#if you want to register more models you do so with additional register() calls.