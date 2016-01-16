from django.conf.urls import include, url
from forum import views as forum
from forum.models import Forum, ExtendForum



urlpatterns = [
    url(r'^$', forum.forum),
    url(r"^page/(?P<page>\d+)/$", forum.forum),
    url(r"^id/(?P<them>\d+)/$", forum.extend_forum),
    url(r"^id/(?P<them>\d+)/ext-them/id/(?P<id>\d+)/$", forum.window_message),
    url(r'^save/$', forum.save_new_them),
    url(r'^extend-them-save/$', forum.seve_new_extend_them),
    url(r'^delete/$', forum.delete_forum),
     url(r'^ext_them_delete/$', forum.ext_them_delete),
    # url(r'^extend-them-save/$', forum.save_new_them, {'model': ExtendForum}),
    # url(r'^enot/$', forum.enot),
]


