from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get_item_by_province/$', views.get_item_by_province, name='get_item_by_province'),
    url(r'^', views.index, name='index'),
]