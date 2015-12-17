from django.shortcuts import render
from forum import forms
from django.http import HttpResponse, Http404, HttpResponseRedirect


def forum(request, model, template, form):
    args = {}
    args['form'] = form
    return render(request, template, args)


def save_new_them(request):
    if request.method == 'POST':
        form = forms.NewThem(request.POST)
        if form.is_valid():
            return forms.NewThem(request, form)
    else:
        form = forms.NewThem()
    return HttpResponse('ok')