from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from data.cartItems import context as cartContext
# from data.itemList import context as itemContext
from user.models import UserList


def register(request):
    return render(request, 'user/register.html')

@csrf_exempt
def login(request):
    if request.method == "POST":
        userName = request.POST.get('user', None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！"
        if userName and password:  # 确保用户名和密码都不为空
            username = userName.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = UserList.objects.get(name=userName)
                if user.password == password:
                    request.session['user'] = user.name
                    return redirect('/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'user/login.html', {"message": message})
    return render(request, 'user/login.html')

@csrf_exempt
def onRegister(request):
    username = request.POST.get('name', None)
    password = request.POST.get('password', None)
    UserList.objects.create(name=username,password=password)
    return render(request, 'user/login.html')
