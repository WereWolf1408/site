from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from publications.models import Publication
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template import RequestContext
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from comment.models import Comment
from pagination.pagination_class import MyPagination
from comment.views import get_comments
from django.views.defaults import page_not_found
from django.core.cache import cache
from django.views.decorators.cache import cache_page

class Publications(object):
    initialization = None

    def __new__(cls, *args, **kwargs):
        if cls.initialization is None:
            cls.initialization = super(Publications, cls).__new__(cls)
        return cls.initialization

    def __init__(self):
        self.records_count = 4
        self.publication = Publication.objects.all()
        self.paginator = Paginator(self.publication, self.records_count)

    def get_page(self, page):
        try:
            publications = self.paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            publications = self.paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            publications = self.paginator.page(self.paginator.num_pages)
        return publications

    def get_pagination(self, page):
        pagination = MyPagination(page=int(page), max_page=int(self.paginator.num_pages)).paginations()
        return pagination


def get_page(request, page):
    args = {}
    args['publications'] = Publications().get_page(page)
    args['pagination'] = Publications().get_pagination(page)
    return render(request, 'newsite_main_page.html', args)


def more(request, pub_id=1):
    try:
        args = {}
        publication = Publications().publication.get(pk=pub_id)
        args['publication'] = publication
        args.update(get_comments(request, pub_id))
        return render_to_response('more.html', args, context_instance=RequestContext(request))
    except ObjectDoesNotExist:
        return HttpResponse('error')


def search(reqeust):
    args = {}
    text = reqeust.GET.get('text')
    publications = Publications().publication.filter(Q(title__icontains=text) | Q(content__icontains=text))
    paginator = Paginator(publications, 10)
    args['publications'] = paginator.page(1)
    return render_to_response('newsite_main_page.html', args, context_instance=RequestContext(reqeust))


# ---------------------------------------------------------------------------------------------------


@cache_page(60 * 15)
def my_cache(request):
    value = Publications().get_page(1)
    return HttpResponse(value)


def ajaxexample(request):
    if 'page' in request.GET:
        page = request.GET.get('page')
        return HttpResponse(page)
    return HttpResponse('(')


