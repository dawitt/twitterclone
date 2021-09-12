from django.contrib import admin
from twitteruser.models import TweeterUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(TweeterUser, UserAdmin)
