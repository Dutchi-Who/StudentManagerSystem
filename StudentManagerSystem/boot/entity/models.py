from django.db import models


class UserInfo(models.Model):  # 用户信息
    username = models.CharField(max_length=32)  # 用户名
    name = models.CharField(max_length=32)  # 姓名
    userId = models.IntegerField()  # 学号
    phone = models.CharField(max_length=32)  # 手机号
    id_card = models.CharField(max_length=32)  # 身份证号
    identity = models.CharField(max_length=32)  # 身份

    def __str__(self):  # 重写__str__方法，使得在后台管理界面显示的是用户名
        return self.username


class Mark(models.Model):  # 成绩
    student = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='studnet')  # 学生
    lesson = models.CharField(max_length=32)  # 课程
    teacher = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='teacher')  # 教师
    score = models.IntegerField()  # 成绩
    create_time = models.DateTimeField(auto_now_add=True)  # 发布时间

    def __str__(self):  # 重写__str__方法
        return self.student.name + '-' + self.lesson + ':' + str(self.score)


class ClassInfo(models.Model):  # 班级
    class_name = models.CharField(max_length=32)  # 班级名称
    grade = models.CharField(max_length=32)  # 年级
    info = models.CharField(max_length=64)  # 简介
    teacher = models.ForeignKey(UserInfo, on_delete=models.CASCADE)  # 班主任
    if_show = models.BooleanField(default=True)  # 班级是否展示

    def __str__(self):  # 重写__str__方法
        return self.class_name


class ClassJoinInfo(models.Model):  # 学生加入班级信息
    class_name = models.ForeignKey(ClassInfo, on_delete=models.CASCADE)  # 班级名称
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)  # 用户
    join_time = models.DateTimeField(auto_now_add=True)  # 加入时间
