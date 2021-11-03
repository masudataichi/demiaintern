from django.contrib import admin

from .models import Submission, User, Thread, Friends

admin.site.register(User)
admin.site.register(Submission)
admin.site.register(Thread)
admin.site.register(Friends)


# Register your models here.
