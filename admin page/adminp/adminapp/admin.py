from django.contrib import admin

from . models import *
from . import models
from . models import Details

# Register your models here.

admin.site.register(User)


@admin.register(models.Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',  'image', 'description','upload_date']