from django.core.mail import send_mail
from django.core.cache import cache
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template.loader import render_to_string

from itsdangerous import URLSafeSerializer
from django.contrib.auth.decorators import login_required

# 注册
# 登录
# 注销
# 修改密码 登录修改  通过邮件修改密码
from apps.main.models import User, ShopCar
from shopping import settings

def login_view(request):
    if request.method == 'GET':
        next = request.GET.get('next')
        return render(request, 'login.html', context={'next': next})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.POST.get('next')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                next = request.POST.get('next')
                next = next if next else '/'
                return redirect(next)
            else:
                msg = "账号或密码有误！！"
                return render(request, 'login.html', {'msg': msg})

        else:
            msg = "账号或密码不能为空！！"
            return render(request, 'login.html', {'msg': msg})
    else:
        return HttpResponse('hhhhh')


def register(request):
    try:
        if request.method == 'GET':
            return render(request, 'register.html')
        elif request.method == 'POST':
            username = request.POST.get('username')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if username and len(phone) == 11 and email and password == confirm_password and len(password) >= 6 and len(
                    password) <= 18:
                user = User.objects.filter(Q(username=username) | Q(phone=phone) | Q(email=email))

                if user.exists():
                    msg = '手机号,用户名或者邮箱已被注册'
                    return render(request, 'register.html', {'msg': msg})
                else:
                    user = User.objects.create_user(phone=phone, username=username, password=password, is_active=0, email=email)
                    if user:
                        user.save()
                        secret = URLSafeSerializer(settings.SECRET_KEY, 'auth')
                        # 用user的id设置一个令牌
                        token = secret.dumps({'name': user.id})
                        # 绑定到缓存redis数据库中 发送过去 并设置过期时间十分钟
                        cache.set(token, user.id, timeout=10 * 60)
                        active_url = f'http:127.0.01:8000/account/active/?token={token}'
                        content = render_to_string(template_name='email.html', request=request,
                                                   context={'user': user, 'active_url': active_url})
                        send_active_email(subject='91商城欢迎你！', content=content, user_email=[email])
                        return redirect('/account/login')
                    else:
                        msg = '网络异常！'
                        return render(request, 'register.html', {'msg': msg})
            else:
                return render(request,'404.html')
    except Exception as  e:
        print(e)


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def update_psword(request):
    pass

def active(request):
    token = request.GET.get('token')
    uid = cache.get(token)
    if uid:
        User.objects.filter(id=uid).update(is_active=1)
        return redirect('/account/login/')
    else:

        return HttpResponse('网络异常!请重新尝试')


'''
send_email() 
    subject 标题
    message 邮件内容
    from_email 发送邮件者
    recipient_list 接受邮件列表
    html_message = 邮件的内容,以html显示发送的内容
    :return:

'''


def user_send_email(request):
    try:
        '''
            用户的密钥过期收到发送密钥
            :param request:
            :return:
            '''
        if request.method == 'GET':
            return render(request, 'active_email.html')
        elif request.method == 'POST':
            value = request.POST.get('value')
            users = User.objects.filter(Q(username=value) | Q(phone=value) | Q(email=value))
            if users.exists():
                secret = URLSafeSerializer(settings.SECRET_KEY, 'auth')
                # 用user的id设置一个令牌
                user = users.first()
                token = secret.dumps({'name': user.id})
                # 绑定到缓存redis数据库中 发送过去 并设置过期时间十分钟
                cache.set(token, user.id, timeout=10 * 60)
                active_url = f'http:127.0.01:8000/account/active/?token={token}'
                content = render_to_string(template_name='email.html', request=request,
                                           context={'user': user, 'active_url': active_url})
                send_active_email(subject='91商城欢迎你！', content=content, user_email=[user.email])
                return redirect('/account/account')
            else:
                msg = '该用户不存在！请前往注册'
                return render(request, 'active_email.html', context={'msg': msg})

    except Exception as e:
        print(e)
        msg = '网络异常！请重试'
        return render(request, 'active_email.html', context={'msg': msg})


def send_active_email(subject='', content=None, user_email=None):
    send_mail(subject=subject, message='', from_email=settings.EMAIL_HOST_USER, html_message=content,
              recipient_list=user_email)
