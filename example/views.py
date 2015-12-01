from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response


def main_page(request, name):
    return render_to_response('newsite_main_page.html', {})