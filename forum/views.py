from django.shortcuts import render
from forum import forms
from django.http import HttpResponse, Http404, HttpResponseRedirect
from forum.models import Forum, ExtendForum
from pagination.pagination_class import MyPagination
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from forum.forms import NewThem, ExtendNewThem


def forum(request, page=None):
    args = {}
    args['form'] = NewThem()
    args.update(get_forum_list(args, Forum, page))
    return render(request, 'forum.html', args)


def extend_forum(request, them=None):
    args= {}
    args['form'] = ExtendNewThem
    args['forum'] = Forum.objects.get(pk=them)
    args.update(get_forum_list(model=ExtendForum, page=1, them=them, args={}))
    return render(request, 'forum-extend-them.html', args)


def window_message(request, them=None, id=None):
    forum = Forum.objects.get(pk=them)
    ext_forum = ExtendForum.objects.get(pk=id)
    return render(request, 'message_window.html', {'forum': forum, 'ext_forum': ext_forum})


def delete_forum(request):
    if 'id' in request.POST:
        id = request.POST.get('id')
        Forum.objects.get(pk=id).delete()
        args = get_forum_list(model=Forum, page=1, args={})
        return render(request, 'forum_content.html', args)
    return HttpResponse('something went wrong')


def ext_them_delete(request):
    if 'id' in request.POST:
        id = request.POST.get('id')
        ExtendForum.objects.get(pk=id).delete()
        args = get_forum_list(model=ExtendForum, page=1, args={})
        return render(request, 'forum_content_ext.html', args)
    return HttpResponse('something went wrong')



def save_new_them(request):
    if 'text' in request.POST:
        text = request.POST.get('text')
        new_forum = Forum(them_name=text, user=request.user)
        new_forum.save()
        args = get_forum_list(model=Forum, page=1, args={})
        return render(request, 'forum_content.html', args)
    return HttpResponse('something went wrong...')


def seve_new_extend_them(request):
    if 'them_id' in request.POST:
        them_id = request.POST.get('them_id')
        text = request.POST.get('text')
        new_extend_forum = ExtendForum(them_name=text, user=request.user, forum_id=them_id)
        new_extend_forum.save()
        args = get_forum_list(model=ExtendForum, page=1, them=them_id, args={})
        args['forum'] = Forum.objects.get(pk=them_id)
        return render(request, 'forum_content_ext.html', args)
    return HttpResponse('something went wrong...')


def get_forum_list(args, model, page, them=None):
    if them is not None:
        list_forum = model.objects.filter(forum_id=them)
    else:
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
    return args