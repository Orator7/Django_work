from django.contrib import admin
from app1.models import Webpage,AccessRecord,Topic

# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
