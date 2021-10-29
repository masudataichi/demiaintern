from django.contrib import admin

from .models import Submission, User

admin.site.register(User)
admin.site.register(Submission)

# Register your models here.
