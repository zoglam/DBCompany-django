from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),

    url(r'^Check/$',  views.Checks, name="Check"),
    url(r'^Client/$',  views.Clients, name="Client"),
    url(r'^Factory/$',  views.Factorys, name="Factory"),
    url(r'^Good/$',  views.Goods, name="Good"),
    url(r'^Payment/$',  views.Payments, name="Payment"),
    url(r'^Transport/$',  views.Transports, name="Transport"),

    url(r'create/', views.create),
    url(r'^Client/(?P<pk>\d+)/$', views.view_client, name='view_client_with_pk'),
    url(r'^Client/(?P<pk>\d+)/edit/$', views.edit_client, name='edit_client'),
    url(r'^Client/(?P<pk>\d+)/delete/$', views.delete_client, name='delete_client'),
    url(r'^Client/(?P<pk>\d+)/check/', views.check_new, name='check_new'), 
    url(r'^Client/(?P<pk>\d+)/payment/', views.payment_new, name='payment_new'),
    url(r'^Check/(?P<pk>\d+)/delete/$', views.delete_check, name='delete_check'),    
    url(r'^Payment/(?P<pk>\d+)/delete/$', views.delete_payment, name='delete_payment'),
    
    url(r'create_factory/', views.create_factory),
    url(r'^Factory/(?P<pk>\d+)/$', views.view_factory, name='view_factory_with_pk'),
    url(r'^Factory/(?P<pk>\d+)/edit/$', views.edit_factory, name='edit_factory'),
    url(r'^Factory/(?P<pk>\d+)/delete/$', views.delete_factory, name='delete_factory'),
    url(r'^Factory/(?P<pk>\d+)/good/', views.good_new, name='good_new'), 
    url(r'^Factory/(?P<pk>\d+)/transport/', views.transport_new, name='transport_new'),
    url(r'^Good/(?P<pk>\d+)/delete/$', views.delete_good, name='delete_good'),    
    url(r'^Transport/(?P<pk>\d+)/delete/$', views.delete_transport, name='delete_transport'),
]
