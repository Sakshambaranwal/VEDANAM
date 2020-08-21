from django.contrib import admin
from .models import Profile
from .models import Account

admin.site.register(Profile)
admin.site.register(Account)