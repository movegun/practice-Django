from django.contrib import admin
from .models import Member,Comment_room,Brand_member,Urls,Ranking,All_url
# Register your models here.


admin.site.register(Member)
admin.site.register(Comment_room)
admin.site.register(Brand_member)
admin.site.register(Urls)
admin.site.register(Ranking)
admin.site.register(All_url)