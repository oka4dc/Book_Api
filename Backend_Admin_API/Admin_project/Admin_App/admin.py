from django.contrib import admin
from Admin_App.models import CustomUser, Group
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Group)

