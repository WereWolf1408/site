from django.conf.urls import include, url
from forum import views as forum
from forum.models import Forum, ExtendForum
from forum.forms import NewThem, ExtendNewThem


urlpatterns = [
    url(r'^$', forum.forum, {'model': Forum, 'template': 'forum.html', 'form': NewThem}),
    url(r"^extend-them/$", forum.forum, {'model': Forum, 'template': 'forum-extend-them.html', 'form': ExtendNewThem}),
]

