from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list', views.list, name='listColors'),
    url(r'^add', views.add, name='addColors'),
    url(r'^get', views.get, name='getColors'),
    url('', views.index, name='index')
]
