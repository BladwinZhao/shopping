import datetime
import json
import random

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django_ajax.decorators import ajax

from apps.main.models import Order, ShopCar
from django.db import transaction


@ajax
@login_required
def confirm_order(request):
    if request.method == 'POST':
        # 接受到的是  Json数据
        cars = request.POST.get('car')
        # 要把它转化为python的数据
        car_list = json.loads(cars)
        if car_list:
            try:
                with transaction.atomic():
                    oid = product_order(request)
                    if oid:
                        for car in car_list:
                            ShopCar.objects.filter(car_id=car.get('car_id')).update(number=car.get('num'), order_id=oid)
                        oid = str(oid)
                        return {'oid': oid}
                    else:
                        msg = '网络异常!'
                        return {'msg': msg}
            except Exception as e:
                print(e)
                transaction.rollback()
        else:
            msg = '网络异常!'
            return {'msg': msg}

    else:
        pass


# 生成订单信息
def product_order(request):
    # 第一步生成订单号  全站必须唯一   尽量大于8位
    user_id = request.user.id
    order_code = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(100000, 999999))
    order = Order(user_id=user_id, order_code=order_code)
    if order:
        order.save()
        return order.oid
    else:
        return None


@login_required
def order(request):
    if request.method == 'GET':
        oid = request.GET.get('oid')
        car_list = ShopCar.objects.filter(order_id=oid)
        all_price=0
        if car_list:
            for car in car_list:
                car.img = car.shop.image_set.values_list('shop_img_id', flat=True)
                all_price =all_price + car.number * car.shop.promote_price
            return render(request, 'order.html', context={'car_list': car_list,'all_price':all_price})
        else:
            pass
    else:
        pass
