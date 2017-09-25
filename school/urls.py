from django.conf.urls import url
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from . import views

app_name = 'school'

urlpatterns =[
    url(r'^$', views.index, name ='index'),
    url(r'^login/$', login, {'template_name': 'pages/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'pages/logout.html'}, name='logout'),
    url(r'^change-password/$', views.change_password, name = 'change_password'),

    url(r'^password-reset/$', password_reset, {'template_name': 'pages/reset_password.html', 
    	                                       'post_reset_redirect':'school:password_reset_done', 
    	                                       'email_template_name': 'pages/reset_password_email.html' },
    	                                        name='reset_password' ),
    
    url(r'^password-reset/done/$', password_reset_done, {'template_name': 'pages/reset_password_done.html'}, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {
        'template_name': 'pages/reset_password_confirm.html',
        'post_reset_redirect':'school:password_reset_complete'},  name='password_reset_confirm'),
    url(r'^password-reset/complete/$', password_reset_complete, {'template_name': 'pages/reset_password_complete.html'}, name='password_reset_complete'),
    url(r'^pupils/list/$', views.show_pupil_list, name='list_pupil'),
    url(r'^teachers/list/$', views.show_teacher_list, name='list_teacher'),
    url(r'^teachers/(?P<id>[0-9]+)/$', views.show_detail_teacher, name='show_detail_teacher'),
    url(r'^teachers/(?P<id>[0-9]+)/edit/$', views.update_teacher, name='update_teacher'),
    url(r'^teachers/add-new/$', views.add_new_teacher, name='add_new_teacher'),
    url(r'^responsibles/list/$', views.show_responsible_list, name='list_responsible'),
     url(r'^responsibles/add-new/$', views.add_new_responsible, name='add_new_responsible'),
    url(r'^responsibles/(?P<id>[0-9]+)/$', views.show_detail_responsible, name='show_detail_responsible'),
    url(r'^responsibles/(?P<id>[0-9]+)/edit/$', views.update_responsible, name='update_responsible'),
    url(r'^courses/list/$', views.show_course_list, name='list_course'),
    url(r'^attendances/list/$', views.show_attendance_list, name='list_attendance'),
    url(r'^scores/list/$', views.show_score_list, name='list_score'),
    url(r'^import/data/$', views.import_data, name='import_data'),
    url(r'^pupils/(?P<id>[0-9]+)/$', views.show_detail_pupil, name='show_detail_pupil'),
    url(r'^pupils/(?P<id>[0-9]+)/edit/$', views.update_pupil, name='update_pupil'),
    url(r'^pupils/add-new/$', views.add_new_pupil, name='add_new_pupil'),

    
    
]