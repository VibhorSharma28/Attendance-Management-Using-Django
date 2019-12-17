from django.contrib import admin

from .models import Record, Detail, Holiday

# Register your models here.
admin.site.register(Record)
admin.site.register(Detail)
admin.site.register(Holiday)