from django.conf.urls import include, url
from comment import views

urlpatterns = [
    url(r'^save/$', views.save),

]
