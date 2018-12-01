from django.conf.urls import url

from apps.shopping_car import views


urlpatterns = [
    url('add/', views.add_car, name='add'),
    url('cars/', views.car_list, name='cars'),
    url('del/(?P<sid>\d+)/', views.delete, name='del',),

]
