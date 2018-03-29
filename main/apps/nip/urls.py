from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new_user/?$', views.new_user),      
    url(r'^login/?$', views.login),
]