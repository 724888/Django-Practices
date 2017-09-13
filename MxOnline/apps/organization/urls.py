# _*_ coding: utf-8 _*_
__author__ = 'LennonChin'
__date__ = '2017/09/12 下午 10:23'

from django.conf.urls import url, include
from views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView

urlpatterns = [

    # 课程机构首页
    url(r'^list/$', OrgView.as_view(), name="list"),
    url(r'^add_ask/$', AddUserAskView.as_view(), name="add_ask"),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="home"),
    url(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name="course"),
]