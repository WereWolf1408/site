from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from publications.models import Publication
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class Publications(object):
    initialization = None

    def __new__(cls, *args, **kwargs):
        if cls.initialization is None:
            cls.initialization = super(Publications, cls).__new__(cls)
        return cls.initialization

    def __init__(self):
        self.publication = Publication.objects.all()
        self.paginator = Paginator(self.publication, 2)

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

    def create_numeration(self):
        mas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        return mas

def main_page(request):
    args = {}
    publications = Publications().publication[:2]
    args['publications'] = publications
    args['request'] = request
    args['numeration'] = Publications().create_numeration()
    return render_to_response('newsite_main_page.html', args)


def get_page(request, page):
    args = {}
    args['publications'] = Publications().get_page(page)
    args['request'] = request
    args['numeration'] = Publications().create_numeration()
    return render_to_response('newsite_main_page.html', args)