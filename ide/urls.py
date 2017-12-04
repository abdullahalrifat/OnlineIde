from django.conf.urls import url
from . import views

app_name='ide'

urlpatterns = [
    url(r'^$', views.ide.as_view(), name='ide'),
    url(r'runc$', views.runc, name='runc'),
    url(r'runcpp$', views.runcpp, name='runcpp'),
    url(r'runpy$', views.runpy, name='runpy'),

]