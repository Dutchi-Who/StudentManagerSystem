import time

from django.http import HttpResponseRedirect
from django.shortcuts import render

from StudentManagerSystem.boot.entity.models import UserInfo, ClassInfo, ClassJoinInfo, Mark


def index(request):
    if request.user.is_authenticated:  # 判断用户是否已登录
        if not UserInfo.objects.filter(username=request.user.username).exists():  # 判断用户信息是否已存在
            return render(request, 'StudentManagerSystem/index.html')
    return HttpResponseRedirect('/login/')


# 首页
def welcome(request):
    if request.user.is_authenticated:  # 判断用户是否已登录
        if not UserInfo.objects.filter(username=request.user.username).exists():  # 判断用户信息是否已存在
            return render(request, 'StudentManagerSystem/pages/welcome.html')
    return HttpResponseRedirect('/login/')


# 学生管理页面
def student(request):
    if request.user.is_authenticated:  # 判断用户是否已登录
        if not UserInfo.objects.filter(username=request.user.username).exists():  # 判断用户信息是否已存在
            return render(request, 'StudentManagerSystem/pages/member/list.html')
    return HttpResponseRedirect('/login/')


# 添加学生
def addStu(request):
    if request.user.is_authenticated:  # 判断用户是否已登录
        if not UserInfo.objects.filter(username=request.user.username).exists():  # 判断用户信息是否已存在
            return render(request, 'StudentManagerSystem/pages/member/add.html')
    return HttpResponseRedirect('/login/')


# 添加学生
def doAddStu(request):
    if request.user.is_authenticated:  # 判断用户是否已登录
        context = {
            'username': request.user.username,
            'name': UserInfo.objects.get(username=request.user.username).name,
            'identity': UserInfo.objects.get(username=request.user.username).identity,
        }
        if request.method == 'POST':
            username = request.POST.get('username')  # 获取班级名称
            grade = request.POST.get('grade')  # 获取表单数据
            class_info = request.POST.get('class_info')  # 获取表单数据
            if_show = request.POST.get('if_show') == "on"

            if UserInfo.objects.filter(username=username).exists():  # 判断班级是否已存在
                request.session['warn'] = "学生已存在!"
                return HttpResponseRedirect('student/add')

            UserInfo.objects.create(
                username=username,
                info=class_info,
                grade=grade,
                teacher=UserInfo.objects.get(username=request.user.username),
                if_show=if_show
            )

            return HttpResponseRedirect('/class-list/')
        return HttpResponseRedirect('/index/')
    else:
        return HttpResponseRedirect('/login/')
