"""
     ____  _      _          _   _   _     _                       
    |  _ \(_) ___| |__      / \ | |_| | __(_)_ __  ___  ___  _ __  
    | |_) | |/ __| '_ \    / _ \| __| |/ /| | '_ \/ __|/ _ \| '_ \ 
    |  _ <| | (__| | | |  / ___ \ |_|   < | | | | \__ \ (_) | | | |
    |_| \_\_|\___|_| |_| /_/   \_\__|_|\_\|_|_| |_|___/\___/|_| |_|

    Copyright Rich Atkinson 2011 All Rights Reserved
"""

import random

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.template import RequestContext

from combos.models import Combo
from flickr.models import Photo


def list_combos(request, template='combos/list_combos.html'):
    """
    List all combos, non-paginated. Kind of a sitemap.
    """
    combos = Combo.objects.all()
    combo_list = []
    for combo in combos:
        photo = Photo.objects.get(uuid=combo.reference)
        if combo.slug:
            combo_list.append((combo, photo))
        
    context_dict = {
        'combo_list': combo_list,
    }
    return render_to_response(template, context_dict, context_instance=RequestContext(request))

def random_combo(request):
    """
    Just deliver a random combo
    """
    combos = Combo.objects.all()
    total = Combo.objects.count()
    try:
        slug = Combo.objects.get(pk=random.randrange(0, total)).slug
        return show_combo(request, slug)   
    except ValueError:
        # probably because there are no combos yet
        return list_combos(request)
        
            
def show_combo(request, slug, template='combos/show_combo.html'):
    """
    Show a combo named by slug
    """
    try:
        combo = Combo.objects.get(slug=slug)
    except MultipleObjectsReturned:
        combos = Combo.objects.filter(slug=slug).order_by('-created')
        if combos.count() > 1:
            for combo in combos[:1]:
                combo.slug = combo.reference
                combo.save()
                return show_combo(request, slug=combo.slug)
    photo = Photo.objects.get(uuid=combo.reference)
    context_dict = {
        'combo': combo,
        'photo': photo,
        'title': '%s ColorCo' % photo.title
    }
    return render_to_response(template, context_dict, context_instance=RequestContext(request))
    
def delete_combo(request, uuid, template='combos/latest_combos.html'):
    """
    Delete a combo, then redirect to the page we were on.
    """
    combo = get_object_or_404(Combo, reference = uuid)
    combo.delete()
    # if page is invalid, default to first
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    return HttpResponseRedirect(reverse(latest_combos) + '?page=%s'%page )
    
def latest_combos(request, order_by='-updated', template='combos/latest_combos.html'):
    """
    Show all combos, paginated, sorted by -updated
    """
    combos = Combo.objects.order_by(order_by)
    paginator = Paginator(combos, 4)
    
    # if page is invalid, default to first
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
        
    # test for out of range
    try:
        combos = paginator.page(page)
    except (EmptyPage, InvalidPage):
        combos = paginator.page(paginator.num_pages)
    
    context_dict = {
        'combo_list': combos,
    }
    return render_to_response(template, context_dict, context_instance=RequestContext(request))
