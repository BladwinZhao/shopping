from django.conf.urls import url

from apps.account import views

urlpatterns = [
    url('login/', views.login_view, name='login'),
    url('register/', views.register, name='register'),
    url('active/', views.active, name='active'),
    url('send/', views.user_send_email, name='send'),
    url('logout/', views.logout_view, name='logout'),

]
