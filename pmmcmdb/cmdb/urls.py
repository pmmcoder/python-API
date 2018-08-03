from django.urls import path
from django.conf.urls import url, include
from . import views,viewsv1,viewsv2,viewsv3,viewsv4,viewsv5,viewsv6
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('spider/', views.spider, name='index'),
#     url(r'^question/$', views.snippet_list),
#     url(r'^question_v4/$', views.snippet_list_v4),
#     url(r'^question_v4/(?P<pk>[0-9]+)$', views.snippet_detail_v4),
#     url(r'^question/(?P<pk>[0-9]+)/$', views.snippet_detail),
#     # path('<str:a>/', views.left, name='index'),

#     url(r'^questionv2/$', viewsv1.SnippetList.as_view()),
#     url(r'^questionv2/(?P<pk>[0-9]+)/$', viewsv1.SnippetDetail.as_view()),

#     url(r'^questionv3/$', viewsv2.SnippetList.as_view()),
#     url(r'^questionv3/(?P<pk>[0-9]+)/$', viewsv2.SnippetDetail.as_view()),

#     url(r'^questionv4/$', viewsv3.SnippetList.as_view()),
#     url(r'^questionv4/(?P<pk>[0-9]+)/$', viewsv3.SnippetDetail.as_view()),

#     url(r'^user/$', viewsv4.UserList.as_view()),
#     url(r'^user/(?P<pk>[0-9]+)/$', viewsv4.UserDetail.as_view()),

#     url(r'^choice/$', viewsv5.ChoiceList.as_view()),
#     url(r'^choice/(?P<pk>[0-9]+)/$', viewsv5.ChoiceDetail.as_view()),

#     url(r'^api/$', viewsv5.api_root),
# ]

# API endpoints
# urlpatterns = [
#     url(r'^$', viewsv5.api_root),
#     url(r'^choices/$',viewsv5.ChoiceList.as_view(),name='choice-list'),
#     url(r'^choices/(?P<pk>[0-9]+)/$',viewsv5.ChoiceDetail.as_view(),name='choice-detail'),
#     url(r'^users/$',viewsv4.UserList.as_view(),name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$',viewsv4.UserDetail.as_view(),name='user-detail')
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)

'''
version 2
'''
# from cmdb.viewsv6 import QuestionViewSet, UserViewSet, api_root, ChoiceViewSet
# from rest_framework import renderers

# question_list = QuestionViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# question_detail = QuestionViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
# choice_list = ChoiceViewSet.as_view({
#     'get': 'list'
# })
# choice_detail = ChoiceViewSet.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = format_suffix_patterns([
#     url(r'^$', api_root),
#     url(r'^questions/$', question_list, name='question-list'),
#     url(r'^questions/(?P<pk>[0-9]+)/$', question_detail, name='question-detail'),
#     url(r'^users/$', user_list, name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
#     url(r'^choices/$', choice_list, name='choice-list'),
#     url(r'^choices/(?P<pk>[0-9]+)/$', choice_detail, name='choice-detail')
# ])


'''
version 3
'''
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'choices', viewsv6.ChoiceViewSet)
router.register(r'users', viewsv6.UserViewSet)
router.register(r'questions', viewsv6.QuestionViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]