from django.conf.urls import url
from . import views

app_name = 'school'

urlpatterns =[
    url(r'^$', views.index, name ='index'),
   
    url(r'^pupils/list/$', views.show_pupil_list, name='list_pupil'),
    url(r'^pupils/(?P<id>[0-9]+)/$', views.show_detail_pupil, name='show_detail_pupil'),
    url(r'^pupils/(?P<id>[0-9]+)/edit/$', views.update_pupil, name='update_pupil'),
    url(r'^pupils/add-new/$', views.add_new_pupil, name='add_new_pupil'),

    url(r'^teachers/list/$', views.show_teacher_list, name='list_teacher'),
    url(r'^teachers/(?P<id>[0-9]+)/$', views.show_detail_teacher, name='show_detail_teacher'),
    url(r'^teachers/(?P<id>[0-9]+)/edit/$', views.update_teacher, name='update_teacher'),
    url(r'^teachers/add-new/$', views.add_new_teacher, name='add_new_teacher'),

    url(r'^responsibles/list/$', views.show_responsible_list, name='list_responsible'),
    url(r'^responsibles/add-new/$', views.add_new_responsible, name='add_new_responsible'),
    url(r'^responsibles/(?P<id>[0-9]+)/$', views.show_detail_responsible, name='show_detail_responsible'),
    url(r'^responsibles/(?P<id>[0-9]+)/edit/$', views.update_responsible, name='update_responsible'),

    url(r'^courses/list/$', views.show_course_list, name='list_course'),
    url(r'^courses/add-new/$', views.add_new_course, name='add_new_course'),
    url(r'^courses/(?P<id>[0-9]+)/$', views.show_detail_course, name='show_detail_course'),
    url(r'^courses/(?P<id>[0-9]+)/edit/$', views.update_course, name='update_course'),

    url(r'^attendances/list/$', views.show_attendance_list, name='list_attendance'),
    url(r'^attendances/add-new/$', views.add_new_attendance, name='add_new_attendance'),
    url(r'^attendances/(?P<id>[0-9]+)/$', views.show_detail_attendance, name='show_detail_attendance'),
    url(r'^attendances/(?P<id>[0-9]+)/edit/$', views.update_attendance, name='update_attendance'),

    url(r'^scores/list/$', views.show_score_list, name='list_score'),
    url(r'^scores/add-new/$', views.add_new_score, name='add_new_score'),
    url(r'^scores/(?P<id>[0-9]+)/edit/$', views.update_score, name='update_score'),
    url(r'^scores/(?P<id>[0-9]+)/$', views.show_detail_score, name='show_detail_score'),

    url(r'^import/data/$', views.import_data, name='import_data'),


    
    
]