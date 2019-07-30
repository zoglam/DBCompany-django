from django.contrib import admin
from accounts.models import Client, UserProfile, Check1, Factory, Good, Payment1, Transport

# Register your models here.
admin.site.register(Check1)
admin.site.register(Client)
admin.site.register(Factory)
admin.site.register(Good)
admin.site.register(Payment1)
admin.site.register(Transport)

admin.site.register(UserProfile)