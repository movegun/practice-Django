from django.contrib import admin
from .models import Member,Comment_room,Brand_member,Urls
# Register your models here.


admin.site.register(Member)
admin.site.register(Comment_room)
admin.site.register(Brand_member)
admin.site.register(Urls)