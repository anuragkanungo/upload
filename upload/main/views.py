# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from upload.main.models import Document
from upload.main.forms import DocumentForm

def list(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            docfile = request.FILES['docfile']
            name = request.POST.get('name')
            docfile.name = name + "_" + docfile.name
            newdoc = Document(docfile = docfile)
            newdoc.save()
            return HttpResponseRedirect(reverse('success'))
    else:
        form = DocumentForm() # A empty, unbound form

    return render_to_response(
        'main/list.html',
        {'form': form},
        context_instance=RequestContext(request)
    )

def success(request):
    return render_to_response('main/success.html',)

