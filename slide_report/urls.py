from django.conf.urls import *
from slide_report import views

urlpatterns = patterns('',
    url('^(?P<name>\w+)/$', views.SlideReportView.as_view(), name='slide-report'),
    url('^(?P<name>\w+)/ajax_preview/$', views.AjaxPreviewView.as_view(), name='slide-preview'),

)
