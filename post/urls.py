from django.conf.urls import url
import views

urlpatterns = [
    # posts
    url(r'posts/$', views.post_list, name='post_list'),
    url(r'^posts/(?P<id>\d+)/$', views.post_detail),
    url(r'^posts/new/$', views.new_post, name='new_post'),
    url(r'^posts/(?P<id>\d+)/edit$', views.edit_post, name='edit'),

    # competition
    url(r'^competition/$', views.show_competition, name='view_comp'),
]