from django.contrib import admin
from .models import Pacs
from .models import Students

# Register your models here.

admin.site.register(Pacs)
admin.site.register(Students)
