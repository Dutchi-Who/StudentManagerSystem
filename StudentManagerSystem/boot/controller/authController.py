from StudentManagerSystem.boot.service import userService


# 登陆页面
def toLog(request):
    return userService.toLog(request)


# 注册页面
def toReg(request):
    return userService.toReg(request)


# 注册操作
def doReg(request):
    return userService.doReg(request)


# 登录操作
def doLog(request):
    return userService.doLog(request)


# 退出登录
def logout(request):
    return userService.logout_action(request)
