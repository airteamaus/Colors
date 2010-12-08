from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.template import RequestContext

from combos.models import Combo
from flickr.models import Photo


def list_combos(request, template='combos/list_combos.html'):
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
    
    
def show_combo(request, slug, template='combos/show_combo.html'):
    combo = Combo.objects.get(slug=slug)
    photo = Photo.objects.get(uuid=combo.reference)
    context_dict = {
        'combo': combo,
        'photo': photo,
    }
    return render_to_response(template, context_dict, context_instance=RequestContext(request))