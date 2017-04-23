from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^save_profiles/$', views.save_profiles, name='save_profiles'),
]
