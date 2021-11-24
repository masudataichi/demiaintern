from django.contrib import admin

from .models import Submission, User, Thread, Friends, Threadlist

admin.site.register(User)
admin.site.register(Submission)
admin.site.register(Thread)
admin.site.register(Friends)
admin.site.register(Threadlist)


# Register your models here.
