from django.conf.urls import url
from . import views

from accounts.views import login_view, register_view, logout_view, user_profile

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', login_view, name='login'),
    url(r'^register/$', register_view, name='register'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^(?P<user_name>[a-zA-Z0-9]+)/$', user_profile, name='profile'),
]