from django.conf.urls import include, url
from forum import views as forum
from forum.models import Forum, ExtendForum



urlpatterns = [
    url(r'^$', forum.forum),
    url(r"^page/(?P<page>\d+)/$", forum.forum),
    # url(r"^(?P<them>\d+)/$", forum.forum),
    url(r'^save/$', forum.save_new_them),
    # url(r'^extend-them-save/$', forum.save_new_them, {'model': ExtendForum}),
    # url(r'^enot/$', forum.enot),
]

