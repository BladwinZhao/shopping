from django.db.models import F
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django_ajax.decorators import ajax

from apps.main.models import ShopCar, Image

'''
验证登录的跳转的连接

'''


@ajax
@login_required
def add_car(request):
    try:
        if request.method == 'POST':
            result = {
                'status': 200,
                'msg': 'succeed',
            }
            number = request.POST.get('number')
            shop_id = request.POST.get('shop_id')
            cars = ShopCar.objects.filter(shop_id=shop_id, user_id=request.user.id, status=1)
            return_number = ShopCar.objects.filter(user_id=request.user.id, status=1).values('shop_id').count()
            if cars.exists():
                car = ShopCar.objects.filter(shop_id=shop_id, user_id=request.user.id, status=1)
                car.update(number=F('number') + number)
            else:
                return_number = return_number + 1
                car = ShopCar(shop_id=shop_id, number=number, user_id=request.user.id)
                car.save()
            result.update(data=return_number)
            return return_number
        else:
            result = {
                'status': 400,
                'msg': 'error',
            }
            return JsonResponse(result)
    except Exception as e:
        result = {
            'status': 400,
            'msg': 'error',
        }
        return JsonResponse(result)


@login_required
def car_list(request):
    car_list = ShopCar.objects.filter(user_id=request.user.id, status=1)
    for car in car_list:
        car.img = Image.objects.filter(shop_id=car.shop_id).values_list('shop_img_id', flat=True).first()
    return render(request, 'car.html', context={'car_list': car_list})


@login_required
def delete(request, sid):
    try:
        if sid:
            cars = ShopCar.objects.filter(shop_id=sid, user_id=request.user.id, status=1)
            if cars:
                cars.update(status=0)
                return redirect('/cart/cars/')
            else:
                msg = '网络异常'
                return render(request, 'car.html', context={'msg': msg})
        else:
            msg = '网络异常'
            return render(request, 'car.html', context={'msg': msg})
    except Exception as e:
        print(e)
        return render(request,'404.html')

