from django.contrib import admin
from django.urls import path

from StudentManagerSystem.boot.controller import authController, indexController

urlpatterns = [
    # Django自带的后台管理
    path('admin/', admin.site.urls),  # 后台管理

    # index首页部分
    path('index/', indexController.index, name='index'),  # 首页
    path('', indexController.index),  # 默认首页

    # 登录部分
    path('login/', authController.toLog, name='login'),  # 登录
    path('register/', authController.toReg, name='register'),  # 注册
    path('login-action', authController.doLog, name='login-action'),  # 登录操作
    path('register-action', authController.doReg, name='register-action'),  # 注册操作
    path('logout/', authController.logout, name='logout'),  # 注销登录

    path('welcome/', indexController.welcome, name='welcome'),  # 首页
    path('student/', indexController.student, name='student'),  # 学生管理
    path('student/add', indexController.addStu, name='addStu'),  # 添加学生
    path('add-action', indexController.doAddStu, name='add-action'),  # 添加学生操作
]
