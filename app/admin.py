from django.contrib import admin
from .models import Member,Slide,RecycleCenter,SlideComment

# Register your models here.

admin.site.register(Member)
admin.site.register(Slide)
admin.site.register(RecycleCenter)
admin.site.register(SlideComment)