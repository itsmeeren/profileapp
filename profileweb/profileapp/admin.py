from django.contrib import admin
from .models import UserProfile


#  -> 1st method
# Register your models here.
admin.site.register(UserProfile)

#I can also register the model like

# ->2 nd method

# @admin.register(UserProfile)
#
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = [ '', '', ]# here i can give the fileds of my data base which required in the adminpanel

