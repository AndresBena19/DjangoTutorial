from django.conf.urls import url

from projectman import views

app_name = 'projectman'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login.as_view(), name='login'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^logout/$', views.logout, name='logout')
]
