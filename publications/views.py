from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from publications.models import Publication
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template import RequestContext
from django.db.models import Q


class Publications(object):
    initialization = None

    def __new__(cls, *args, **kwargs):
        if cls.initialization is None:
            cls.initialization = super(Publications, cls).__new__(cls)
        return cls.initialization

    def __init__(self):
        self.records_count = 3
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


def get_page(request, page):
    args = {}
    args['publications'] = Publications().get_page(page)
    return render_to_response('newsite_main_page.html', args, context_instance=RequestContext(request))


def more(request, id):
    publication = Publications().publication.get(id=id)
    return render_to_response('more.html', {'publication': publication}, context_instance=RequestContext(request))


def search(reqeust):
    args = {}
    text = reqeust.GET.get('text')
    publications = Publications().publication.filter(Q(title__icontains=text) | Q(content__icontains=text))
    paginator = Paginator(publications, 10)
    args['publications'] = paginator.page(1)
    return render_to_response('newsite_main_page.html', args, context_instance=RequestContext(reqeust))


def ajaxexample(request):
    return HttpResponse('this is ajax example')
