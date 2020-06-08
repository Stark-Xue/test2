from django.shortcuts import render, HttpResponse, redirect
import os
from django.views import View
from django.urls import reverse
from app01 import models

# Create your views here.

# USER_DICT = {
#     '1' : 'root1',
#     '2' : 'root2',
#     '3' : 'root3',
# }
USER_DICT = {
    '1' : {'name':'root1', 'email':'root@live.com'},
    '2' : {'name':'root2', 'email':'root@live.com'},
    '3' : {'name':'root3', 'email':'root@live.com'},
    '4' : {'name':'root4', 'email':'root@live.com'},
}

def index(request):
    #return HttpResponse("index")
    #print(request.path_info)
    #v = reverse('indexx', args=(90, ))
    #print(v)
    #return render(request, 'index.html', {'user_dict':USER_DICT})
    return render(request, 'index.html')

def user_info(request):
    if request.method == "GET":
        # QuerySet [obj(id,username,email,user_group_id,user_group_id(uid, caption)), obj]
        user_list = models.UserInfo.objects.all()
        # print(user_list.query)
        # for row in user_list:
        #     print(row.id)
        #     print(row.user_group)
        #     print(row.user_group.uid)
        group_list = models.UserGroup.objects.all()
        for row in group_list:
            print(row.caption)
        return render(request, 'user_info.html', {'user_list': user_list, 'group_list': group_list})
    elif request.method == "POST":
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        models.UserInfo.objects.create(username=u, password=p)
        return redirect('/cmdb/user_info/')

def user_detail(request, nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    # 取单条数据，如果不存在，就直接报错
    # models.UserInfo.objects.get(id=nid)
    return render(request, 'user_detail.html', {'obj': obj})

def user_del(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/cmdb/user_info/')

def user_edit(request, nid):
    if request.method == "GET":
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request, "user_edit.html", {'obj': obj})
    elif request.method == "POST":
        nid = request.POST.get('id')
        u = request.POST.get('username')
        p = request.POST.get('password')
        models.UserInfo.objects.filter(id=nid).update(username=u, password=p)
        return redirect('/cmdb/user_info/')

def detail(request, n): # def detail(request, *args, **kwargs):
    #return HttpResponse(n)
    #nid = request.GET.get('n')
    detail_info = USER_DICT[n]
    return render(request, 'detail.html', {'detail_info':detail_info})

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        # way 1 选择这个比较合适
        obj = models.UserInfo.objects.filter(username=u, password=p).first()
        # way 2 不建议  
        # count = models.UserInfo.objects.filter(username=u, password=p).count()
        print(obj) # obj None
        if obj:
            return redirect('/cmdb/index/')
        else:
            #return redirect('/login/')
            return render(request, 'login.html')
    else:
        return redirect('/index/')

def regist(request):
    if request.method == 'GET':
        return render(request, 'regist.html')
    elif request.method == 'POST':
        v = request.POST.get('gender')
        print(v)
        x = request.POST.getlist('favor')
        print(x)
        y = request.POST.get('fafafa')
        print(y)
        obj = request.FILES.get('fafafa')
        print(obj, type(obj), obj.name)

        file_path = os.path.join('upload', obj.name)
        f = open(file_path, mode='wb')
        for i in obj.chunks():
            f.write(i)
        f.close()

        return render(request, 'regist.html')
    else:
        return redirect('/index/')

class Home(View):

    def dispatch(self, request, *args, **kwargs):
        #调用父类的dispatch
        print('before')
        result = super(Home, self).dispatch(request, *args, **kwargs)
        print('after')
        return result

    def get(self, request):
        print(request.method)
        return render(request, 'home.html')

    def post(self, request):
        print(request.method)
        return render(request, 'home.html')

def orm(request):
    # 创建
    # 1、
    models.UserInfo.objects.create(username='root', password='123')
    #models.UserGroup.objects.create(caption="dba")
    
    # 2、
    dic = {'username': 'test', 'password': '123'}
    models.UserInfo.objects.create(**dic)

    # 3、
    obj = models.UserInfo(username='severen', password="123")
    obj.save()

    # 查
    # result = models.UserInfo.objects.all()
    # result是一个QuerySet类型，这个类型是Django提供的，我们去理解的就话，就当它是一个列表即可，列表内的元素是UserInfo的对象
    result = models.UserInfo.objects.filter(username='root')
    result = models.UserInfo.objects.filter(username='root', password='123')
    for row in result:
        print(row.id, row.username, row.password)

    # 删除
    #models.UserInfo.objects.all().delete()
    # models.UserInfo.objects.filter(id=4).delete()

    # 更新
    # models.UserInfo.objects.all().update(password='666')
    # gte -> 大于等于；lte -> 小于等于
    # models.UserInfo.objects.filter(id__gt=1).update(password='666') # id > 1


    
    return HttpResponse('orm')