from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from comment.models import Comment
from publications.models import Publication
from django.core.exceptions import ObjectDoesNotExist
from pagination.pagination_class import MyPagination
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def save(request):
    if request.user.is_authenticated():
        if 'text' in request.POST:
            pub_id = Publication.objects.get(id=request.POST.get('id'))
            us = request.user
            comment = Comment(text=request.POST.get('text'), publication=pub_id, user=us)
            comment.save()
            return get_ajax_comments(request, pub_id)
    return HttpResponse('wrong!')


def get_ajax_comments(request, pub_id):
    args = {}
    args.update(get_comments(request, pub_id))
    return render(request, 'comment_body.html', args)


def get_comments(request, pub_id):
    args = {}
    page = 1
    if 'page' in request.POST:
        page = request.POST.get('page')
    comments = Comment.objects.filter(publication_id=pub_id)
    paginator = Paginator(comments, 5)

    try:
        args['comments'] = paginator.page(page)
    except PageNotAnInteger:
        args['comments'] = paginator.page(1)
    except EmptyPage:
        args['comments'] = paginator.page(paginator.num_pages)
    return get_comment_pagination(args=args, paginator=paginator, page=page)


def get_comment_pagination(args, paginator, page):
    args['pagination'] = MyPagination(max_page=paginator.num_pages, page=page).paginations()
    print('pagination', args['pagination'])
    return args

