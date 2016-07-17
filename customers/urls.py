from django.conf.urls import url
from . import views

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
	url(r'^$', views.index),
	url(r'^user/customer/$', views.customer_view),
	url(r'^user/(?P<method>create)/$', views.user_view),
	url(r'^user/(?P<method>update)/$', views.user_view),
	url(r'^user/(?P<method>list)/$', views.user_view),
	url(r'^user/name/$', views.name_view),
	url(r'^user/checkpassword/$', views.checkpassword_view),
	url(r'^user/setpassword/$', views.setpassword_view),
	url(r'^profile/$', views.profile_view),
	url(r'^profile/(?P<username>\w+)/$', views.profile_view),
	url(r'^login/$', views.login_view),
]
