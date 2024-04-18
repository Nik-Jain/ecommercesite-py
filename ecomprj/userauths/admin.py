from django.contrib import admin
from userauths import models
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'bio']

admin.site.register(models.User, UserAdmin)