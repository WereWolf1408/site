from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from authentication.form import AuthenticationForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout


def auth_reg_form(request, model, template, reg_log_func):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = model(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data['your_name']
            return reg_log_func(request, form)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = model()
    return render(request, template, {'form': form})

def log_in(request, form):
    username = form.cleaned_data['your_name']
    password = form.cleaned_data['password']
    user = authenticate(username='test', password='test')
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/site/')
    else:
        return HttpResponse('error')


def registration(request, form):
    pass


def log_out(request):
    logout(request)
    return redirect('/site/')