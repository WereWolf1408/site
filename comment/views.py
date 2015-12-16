from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from comment.models import Comment
from publications.models import Publication
from django.core.exceptions import ObjectDoesNotExist


def save(request):
    if request.user.is_authenticated():
        if 'text' in request.POST:
            pub = Publication.objects.get(id=request.POST.get('id'))
            us = request.user
            comment = Comment(text=request.POST.get('text'), publication=pub, user=us)
            comment.save()
            return get_comment(request, pub)
    return HttpResponse('wrong!')


def get_comment(request, pub):
    comments = Comment.objects.filter(pk=pub.id)[:5]
    return render_to_response('comment_body.html', {'comments': comments})

