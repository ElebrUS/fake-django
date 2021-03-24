from django.contrib import admin
from .models import Schema, Column, DataType, Data

# Register your models here.
admin.site.register(Schema)
admin.site.register(Column)
admin.site.register(DataType)
admin.site.register(Data)
