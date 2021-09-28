#from django.urls import path
from django.conf.urls import url
from .views import (PostListView,
					PostDetailView,
					PostCreateView,
					PostUpdateView,
					PostDeleteView,
					PostTestView
                   )

app_name = 'board'

urlpatterns = [
		url(r'^$', PostListView.as_view() , name='notice-board' ),
		url(r'^posts/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-detail'),
		url(r'^posts/new', PostCreateView.as_view(), name='post-create'),
		url(r'^posts/(?P<pk>\d+)/edit/', PostUpdateView.as_view(), name='post-update'),
		url(r'^posts/(?P<pk>\d+)/delete/', PostDeleteView.as_view(), name='post-delete'),
		url(r'^posts/js', PostTestView.as_view(), name='post-test'),
]
