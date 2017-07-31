from django.conf.urls import url
from . import views

app_name = 'items'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^add/$', views.ItemCreate.as_view(), name='item-add'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.ItemUpdate.as_view(), name='item-update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.ItemDelete.as_view(), name='item-delete'),
]