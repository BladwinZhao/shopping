from django.db.models import F
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django_ajax.decorators import ajax

from apps.main.models import ShopCar

'''
验证登录的跳转的连接

'''
@ajax
@login_required
def add_car(request):
    try:
        if request.method == 'GET':
            result = {
                'status': 200,
                'msg': 'succeed',
            }
            number = request.GET.get('number')
            shop_id = request.GET.get('shop_id')
            cars = ShopCar.objects.filter(shop_id=shop_id, user_id=request.user.id, status=1)
            return_number = ShopCar.objects.filter(user_id =request.user.id,status=1).values('shop_id').count()
            if cars.exists():
                car = ShopCar.objects.filter(shop_id=shop_id, user_id=request.user.id, status=1)
                car.update(number=F('number') + number)
            else:
                return_number =return_number+ 1
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

def car_list(request):
    pass



def delect(request):
    pass
