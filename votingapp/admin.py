from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Department)

class voterAdmin(admin.ModelAdmin):
    list_display = ['name','reg_no','department','stage']

admin.site.register(Voter,voterAdmin)

class deligateAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','position','department','reg_no','vote']
    ordering = ['vote']

admin.site.register(Deligate,deligateAdmin)
