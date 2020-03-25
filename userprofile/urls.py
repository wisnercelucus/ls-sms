from django.conf.urls import url
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from . import views

app_name = 'userprofile'



urlpatterns =[
	url(r'^$', views.profile, name='profile'),
    url(r'^login/$', login, {'template_name': 'userprofile/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'userprofile/logout.html'}, name='logout'),
    url(r'^change-password/$', views.change_password, name = 'change_password'),

    url(r'^password-reset/$', password_reset, {'template_name': 'userprofile/reset_password.html', 
    	                                       'post_reset_redirect':'userprofile:password_reset_done', 
    	                                       'email_template_name': 'userprofile/reset_password_email.html' },
    	                                        name='reset_password' ),
    
    url(r'^password-reset/done/$', password_reset_done, {'template_name': 'userprofile/reset_password_done.html'}, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {
        'template_name': 'userprofile/reset_password_confirm.html',
        'post_reset_redirect':'userprofile:password_reset_complete'},  name='password_reset_confirm'),
    url(r'^password-reset/complete/$', password_reset_complete, {'template_name': 'userprofile/reset_password_complete.html'}, name='password_reset_complete'),
        
    
]