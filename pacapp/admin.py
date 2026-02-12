from django.contrib import admin
from models import Offices
from models import Specializations
from models import Pacs
from models import Students
from models import PastoralNotes

# Register your models here.

admin.site.register(Offices)
admin.site.register(Specializations)
admin.site.register(Pacs)
admin.site.register(Students)
admin.site.register(PastoralNotes)

