from django.contrib import admin

# Register your models here.from django.contrib import admin

# Register your models here.
from .models import User
from .models import Project

admin.site.register(User)
admin.site.register(Project)
