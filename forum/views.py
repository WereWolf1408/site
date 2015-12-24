from django.shortcuts import render
from forum import forms
from django.http import HttpResponse, Http404, HttpResponseRedirect
from forum.models import Forum
from pagination.pagination_class import MyPagination
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from forum.forms import NewThem, ExtendNewThem


def forum(request, page=None):
    args = {}
    args['form'] = NewThem()
    args.update(get_forum_list(args, Forum, page))
    return render(request, 'forum.html', args)



def save_new_them(request):
    if 'text' in request.POST:
        text = request.POST.get('text')
        new_forum = Forum(them_name=text, user=request.user)
        new_forum.save()
        args = get_forum_list(model=Forum, page=1, args={})
        return render(request, 'forum_content.html', args)
    return HttpResponse('something went wrong...')


def get_forum_list(args, model, page):
    list_forum = model.objects.all()
    paginator = Paginator(list_forum, 10)
    try:
        args['forum_list'] = paginator.page(page)
    except PageNotAnInteger:
        args['forum_list'] = paginator.page(1)
    except EmptyPage:
        args['forum_list'] = paginator.page(paginator.num_pages)
    return get_forum_pagination(args=args, paginator=paginator, page=page)


def get_forum_pagination(args, page, paginator):
    args['pagination'] = MyPagination(max_page=paginator.num_pages, page=page).paginations()
    print('pagination', args['pagination'])
    return args