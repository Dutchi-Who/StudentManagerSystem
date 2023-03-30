from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render

from StudentManagerSystem.boot.entity.models import UserInfo


def user_info(request):  # 用户信息
    if request.user.is_authenticated:  # 判断用户是否已登录
        if not UserInfo.objects.filter(username=request.user.username).exists():  # 判断用户信息是否已存在
            return HttpResponseRedirect('/reg-detail/')
        context = {  # 将数据传递给前端
            'username': request.user.username,
            'email': request.user.email,
            'name': UserInfo.objects.get(username=request.user.username).name,
            'phone': UserInfo.objects.get(username=request.user.username).phone,
            'userId': UserInfo.objects.get(username=request.user.username).userId,
            'id_card': UserInfo.objects.get(username=request.user.username).id_card,
            'identity': UserInfo.objects.get(username=request.user.username).identity,
        }
        if request.session.get('info', False):  # 判断是否有提示信息
            context['info'] = request.session.pop('info')
        if request.session.get('warn', False):  # 判断是否有警告信息
            context['warn'] = request.session.pop('warn')
        return render(request, 'StudentManagerSystem/user-info.html', context)
    else:
        return HttpResponseRedirect('/login/')


def user_info_action(request):  # 修改用户信息
    if request.user.is_authenticated:  # 判断用户是否已登录
        if not UserInfo.objects.filter(username=request.user.username).exists():  # 判断用户信息是否已存在
            return HttpResponseRedirect('/reg-detail/')
        if request.method == 'POST':  # 判断请求方式
            user = UserInfo.objects.get(username=request.user.username)  # 获取用户信息
            user.name = request.POST.get('name')
            user.phone = request.POST.get('mobile')
            user.userId = request.POST.get('userId')
            user.id_card = request.POST.get('id_card')
            user.identity = request.POST.get('identity')
            user.save()  # 保存数据
            request.session['info'] = '个人信息修改成功！'
        return HttpResponseRedirect('/user-info/')
    else:
        return HttpResponseRedirect('/login/')


def user_pass_action(request):  # 修改密码
    if request.user.is_authenticated:  # 判断用户是否已登录
        if not UserInfo.objects.filter(username=request.user.username).exists():  # 判断用户信息是否已存在
            return HttpResponseRedirect('/reg-detail/')
        if request.method == 'POST':  # 判断请求方式
            user = request.user
            if request.POST.get('newPass') != request.POST.get('confirmPass'):  # 判断两次输入的密码是否一致
                request.session['warn'] = '两次输入的密码不一致！'
                return HttpResponseRedirect('/user-info/')
            if user.check_password(request.POST.get('newPass')):  # 判断新密码是否与旧密码一致
                request.session['warn'] = '新密码与原密码相同！'
                return HttpResponseRedirect('/user-info/')
            if user.check_password(request.POST.get('oldPass')):  # 判断旧密码是否正确
                user.set_password(request.POST.get('newPass'))
                user.save()
                login(request, user)
                request.session['info'] = '密码修改成功！'
                return HttpResponseRedirect('/user-info/')
            request.session['warn'] = '原密码不正确！'  # 旧密码不正确
            return HttpResponseRedirect('/user-info/')
    else:
        return HttpResponseRedirect('/login/')
