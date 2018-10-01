from django.shortcuts import render
from django.http import HttpResponse
from collections import defaultdict

from search_app.forms import *
from search_app.models import *


fields = {
    "wordform": "wordform",
    "lemma": "lemma",
    "pos": "pos__in",
    "mistake": "mistake__tag__in",
    "sentence": "sentence__pk__in"
}
    
    
def structure_word_query(query_dict):
    print(query_dict)
    query_by_word = defaultdict(dict)
    for k, v in query_dict.items():
        print(k)
        generic_key, n = k.rsplit('_', 1)
        query_by_word[int(n)][generic_key] = v
    final_query_by_word = []
    for i, k in enumerate(query_by_word):
        final_query_by_word.append(query_by_word[k])
    return final_query_by_word
    
    
def get_word_results(query):
    values = {
        fields[param]:query[param]
        for param in query
        if param in fields and query[param]
    }
    #print(values)
    results = Word.objects.filter(**values)
    return results

    
def exact_search(request):
    if request.GET:
        form = ExactMatchForm(request.GET)
        if form.is_valid():
            text = form.cleaned_data['exact_query']
            results = Sentence.objects.filter(sentence__icontains = text)
            return HttpResponse([(x.sentence, x.text.pk) for x in results])
    else:
        form = ExactMatchForm()

    return render(request, 'search.html', {'form': form})
    

    
def word_search(request):
    if request.GET:
        structured_query = structure_word_query(request.GET)
        first_word_results = get_word_results(structured_query[0])
        sentences = {x.sentence.pk for x in first_word_results}
        results = first_word_results
        for i in range(1, len(structured_query)):
            if sentences:
                structured_query[i]['sentences'] = sentences
                word_results = get_word_results(structured_query[i])
                sentences &= {x.sentence.pk for x in word_results}
                results |= word_results
            else:
                results = []
        results = results.filter(**{fields['sentence']: sentences})
        return HttpResponse([(x.wordform, x.sentence.sentence) for x in results])
    else:
        form = WordSearchForm()
        nextform = NextWordSearchForm()

    return render(request, 'search.html', {'form': form, 'nextform': nextform})