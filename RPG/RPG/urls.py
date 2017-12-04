from django.views.generic.base import TemplateView
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
urlpatterns = [

    url(r'^$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^$', TemplateView.as_view(template_name='../character/templates/character/home.html'), name='home'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^character/', include('character.urls')),
    url(r'^admin/', admin.site.urls),
]
