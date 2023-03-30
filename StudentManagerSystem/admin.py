from django.contrib import admin

from StudentManagerSystem.boot.entity.models import UserInfo, Mark, ClassInfo

admin.site.register(UserInfo)
admin.site.register(Mark)
admin.site.register(ClassInfo)
