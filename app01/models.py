from django.db import models

# Create your models here.

#app01_userinfo
class UserInfo(models.Model):
    #  隐含的，自动创建id列，自增，主键
    # 用户名列、字符串类型、指定长度
    # 字段：字符串、数字、时间、二进制、自增(primary_key)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=60)
    test = models.EmailField(max_length=19, null=True, error_messages={'invalid': '请输入密码'})
    # genger = models.CharField(max_length=60, null=True)
    user_group = models.ForeignKey("UserGroup", to_field='uid', default=1, on_delete=models.CASCADE)
    user_type_choices = (
        (1, '超级用户'),
        (1, '普通用户'),
        (1, '普普通用户'),
    )
    user_type_id = models.IntegerField(choices=user_type_choices, default=1)

class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32)
    ctime = models.DateTimeField(auto_now_add=True, null=True)
    uptime = models.DateTimeField(auto_now=True, null=True)