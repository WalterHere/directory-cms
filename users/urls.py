from django.conf.urls import url

from wagtail.users.views import users as original_users_views

from . import views

app_name = 'great_users'
urlpatterns = [
    url(r'^$', original_users_views.Index, name='index'),
    url(r'^add/$', views.CreateUserView.as_view(), name='add'),
    url(r'^(?P<pk>\d+)/$', views.EditUserView.as_view(), name='edit'),
    url(r'^([^\/]+)/delete/$', original_users_views.Delete, name='delete'),
]
