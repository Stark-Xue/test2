from django.shortcuts import render, HttpResponse, redirect
import os
from django.views import View
from django.urls import reverse

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

def index(request, nid):
    #return HttpResponse("index")
    print(request.path_info)
    v = reverse('indexx', args=(90, ))
    print(v)
    return render(request, 'index.html', {'user_dict':USER_DICT})

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
        if u == 'severen' and p == '123':
            return redirect('/index/')
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