from django.contrib import admin

from .models import Submission, User, Thread

admin.site.register(User)
admin.site.register(Submission)
admin.site.register(Thread)

# Register your models here.
