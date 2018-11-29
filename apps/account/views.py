from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# 注册
# 登录
# 注销
# 修改密码 登录修改  通过邮件修改密码

def login_view(request):
    if request.method == 'GET':
        next = request.GET.get('next')
        return render(request,'login.html', context={'next': next})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.POST.get('next')
        if username and password:
            user = authenticate(username=username, password=password)
            if user.exists():
                login(request, user)
                next =request.POST.get('next')
                next =next if next else '/'
                return redirect(next)
            else:
                msg = "账号或密码有误！！"
                render(request, 'login.html', {'msg': msg})

        else:
            msg = "账号或密码不能为空！！"
            render(request, 'login.html', {'msg': msg})
    else:
        return HttpResponse('hhhhh')



def register(request):
    if request.method =='GET':
        return render(request,'register.html')
    elif request.method=='POST':
        pass



