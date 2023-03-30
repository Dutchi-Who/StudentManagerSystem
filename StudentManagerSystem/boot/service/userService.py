from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import request, HttpResponseRedirect
from django.shortcuts import render


# 跳转到登录页
def toLog(data):
    if data.user.is_authenticated:  # 判断用户是否已登录
        return HttpResponseRedirect('/index/')  # 已经登录，直接跳转到首页
    return render(data, 'StudentManagerSystem/login.html')  # 未登录，跳转到登陆页面


# 跳转到注册页面
def toReg(data):
    if data.user.is_authenticated:  # 判断用户是否已登录
        return HttpResponseRedirect('/index/')  # 已经登录，直接跳转到首页
    return render(data, 'StudentManagerSystem/register.html')  # 未登录，跳转到注册页面


# 登录操作
def doLog(data):
    username = data.POST.get('loginUsername')  # 获取用户名
    password = data.POST.get('loginPassword')  # 获取密码
    user = authenticate(data, username=username, password=password)  # 验证用户名和密码
    if username == '' or password == '':  # 判断是否有空值
        return render(data, 'StudentManagerSystem/index.html',
                      {'warn': '用户名或密码不能为空！', 'username': username})
    if user is not None:  # 判断用户是否登陆成功
        print("登录成功")
        login(data, user)
        data.session['info'] = "欢迎回来，" + username + "！"
        return HttpResponseRedirect('/')
    else:  # 登陆失败
        print("登录失败")
        return render(data, 'StudentManagerSystem/login.html', {'error': '用户名或密码错误！', 'username': username})


# 注册操作
def doReg(data):
    username = data.POST.get('registerUsername')  # 获取用户名
    email = data.POST.get('registerEmail')  # 获取邮箱
    password = data.POST.get('registerPassword')  # 获取密码

    print(username)
    # 判断是否有空值
    if username == '' or email == '' or password == '':
        return render(data, 'StudentManagerSystem/register.html',
                      {'warn': '用户名、邮箱或密码不能为空！', 'username': username, 'email': email})
    # 判断用户名是否已存在
    if User.objects.filter(username=username).exists():
        return render(data, 'StudentManagerSystem/register.html',
                      {'warn': '用户名已存在！', 'email': email})
    # 判断邮箱是否已存在
    if User.objects.filter(email=email).exists():
        return render(data, 'StudentManagerSystem/register.html',
                      {'warn': '此邮箱已经注册！请登录或找回密码！', 'username': username})
    # 持久层缓存用户信息
    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()  # 保存用户
    login(data, user)  # 登录
    return HttpResponseRedirect('/index/')  # 跳转到首页


# 退出登录
def logout_action(data):  # 注销操作
    if data.user.is_authenticated:  # 判断用户是否已登录
        logout(data)  # 注销
    return HttpResponseRedirect('/login/')
