from django.conf.urls import url

from search import views

"""
url('detail' shop.shop_id)'
"""
urlpatterns = [
    url('result/', views.search, name='search')
]
