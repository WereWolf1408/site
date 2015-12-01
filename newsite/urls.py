"""newsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from example import views
from publications import views as pub
from authentication import views as auth
from authentication.form import AuthenticationForm, RegistrationForm

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^site/page/([0-9])/$', pub.get_page),
    url(r'^site/page/([0-9]{2})/$', pub.get_page),
    url(r'^site/$', pub.main_page),
    url(r'^authentication/$', auth.auth_reg_form, {'model': AuthenticationForm, 'template': 'authentication_form.html',
                                                   'reg_log_func': auth.log_in}),
    url(r'^registration/$', auth.auth_reg_form, {'model': RegistrationForm, 'template': 'registration_form.html',
                                                 'reg_log_func': auth.registration}),
    url(r'^log_out/$', auth.log_out)
]
