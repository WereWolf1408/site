from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from authentication.form import AuthenticationForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


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


def form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AuthenticationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data['your_name']
            return AuthenticationForm(request, form)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AuthenticationForm()
    return render(request, '404.html', {'form': form})

def log_in(request, form):
    username = form.cleaned_data['your_name']
    password = form.cleaned_data['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/site/')
    else:
        return HttpResponse('error')


def registration(request, form):
    try:
        username = form.cleaned_data['your_name']
        password = form.cleaned_data['password']
        email = form.cleaned_data['emain']
        user = User.objects.get(email=email)
        return HttpResponse('user with the email= ' + user.email + ' already exists')
    except ObjectDoesNotExist:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return log_in(request, form)


def log_out(request):
    logout(request)
    return redirect('/site/')