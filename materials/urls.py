from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^c/(\d+)/$', views.index_detail, name='index_c'),

	url(r'^incoming/$', views.incoming, name='incoming'),
	url(r'^incoming/p(\d+)/$', views.incoming_pallet, name="incoming_p"),
	url(r'^incoming/c(\d+)/$', views.incoming_customer, name="incoming_c"),
	url(r'^incoming/z(\d+)/$', views.incoming_zone, name="incoming_z"),
	url(r'^incoming/m(\d+)/$', views.incoming_material, name="incoming_m"),
	
	url(r'^outgoing/$', views.outgoing, name='outgoing'),
	url(r'^outgoing/p(\d+)/$', views.outgoing_pallet, name="outgoing_p"),
	url(r'^outgoing/c(\d+)/$', views.outgoing_customer, name="outgoing_c"),
	url(r'^outgoing/z(\d+)/$', views.outgoing_zone, name="outgoing_z"),
	url(r'^outgoing/m(\d+)/$', views.outgoing_material, name="outgoing_m"),

	url(r'^result/$', views.result, name='result'),
	url(r'^result/c(\d+)/$', views.result, name='result_c'),
	url(r'^result/m(\S+)/$', views.result_detail, name='result_detail'),
	# url(r'^outgoing/$', views.OutgoingList.as_view(), name='outgoing_list'),
	
	# url(r'^material/(?P<pk>\d+)/$', views.MaterialDetail.as_view(), name='material_detail'),
	# url(r'^incoming/(?P<pk>\d+)/$', views.IncomingDetail.as_view(), name='incoming_detail'),
	# url(r'^outgoing/(?P<pk>\d+)/$', views.OutgoingDetail.as_view(), name='outgoing_detail'),

	# url(r'^outgoing/(?P<customer_id>\d+)/$', views.outgoing_detail, name='detail'),
	# url(r'^outgoing/(?P<customers>)/submit/$', views.submit, name='submit'),
	# url(r'^outgoing/(?P<customers>)/result/$', views.result, name='result'),
]
