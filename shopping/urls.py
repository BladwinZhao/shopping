import xadmin
from django.conf.urls import url, include
from django.conf.urls.static import static

from apps.main import views
from shopping import settings

urlpatterns = [
                  url('xadmin/', xadmin.site.urls),
                  url('^$', views.index),
                  url('shop/', include('detail.urls')),
                  url('search/', include('search.urls')),
                  url('account/', include('account.urls')),
                  url('cart/', include('shopping_car.urls')),
                  url('order/', include('order.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
