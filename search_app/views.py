from django.shortcuts import render
from django.http import HttpResponse

from search_app.forms import *
from search_app.search_funcs import *

    
def exact_search(request):
    if request.GET:
        form = ExactMatchForm(request.GET)
        if form.is_valid():
            text = form.cleaned_data['exact_query']
            results = exact_search(text)
            return HttpResponse([(x.sentence, x.text.pk) for x in results])
    else:
        form = ExactMatchForm()

    return render(request, 'search.html', {'form': form, 'use_js': False})   
    
    
def word_search(request):
    if request.GET:
        results = search_detailed(request.GET.lists())
        return HttpResponse([(x.wordform, x.pk, x.pos, x.sentence.sentence) for res in results for x in res])
    else:
        form = WordSearchForm()
        nextform = NextWordSearchForm()

    return render(request, 'search.html', {'form': form, 'nextform': nextform, 'use_js': True})
    
    
def mistake_search(request):
    if request.GET:
        results = get_mistake_results(request.GET.lists())
        return HttpResponse([(x.text, x.correction, x.sentence.sentence) for x in results])
    else:
        form = MistakeSearchForm()

    return render(request, 'search.html', {'form': form, 'use_js': False})
        