from django.conf.urls import url,include
from hearthstone import views

app_name = 'hearthstone'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail')
]
