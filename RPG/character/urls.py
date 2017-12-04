from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^all/$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^$', views.HomeView.as_view(), name='home')


]