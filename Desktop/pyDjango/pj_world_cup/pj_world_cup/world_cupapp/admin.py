from django.contrib import admin
from .models import *
# Register your models here.


# @admin.register(Item)
# class ItemAdmin(admin.ModelAdmin):
# 	pass



# print(inspect.getmembers(models.modules["apps.world_cupapp.models"]))
# modelClasses = [
        
#         ]

# for x in inspect.getmembers(sys.modules["apps.world_cupapp.models"], inspect.isclass):
#         if models.Model in x[1].__bases__

# print(modelClasses)

# admin.site.register(Item, ItemAdmin)
admin.site.register(Member)
admin.site.register(Comment_room)
admin.site.register(Brand_member)
admin.site.register(Urls)
admin.site.register(Ranking)

admin.site.register(Comment_test)