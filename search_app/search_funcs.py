from collections import defaultdict
from django.utils.datastructures import MultiValueDict
from search_app.models import *

word_fields = {
    "wordform": ("wordform", "str"),
    "lemma": ("lemma", "str"),
    "pos": ("pos__in", "list"),
    "mistake": ("mistake__tag__in", "list"),
    "sentence": ("sentence__pk__in", "list")
}

mistake_fields = {
    "text": ("text__icontains", "str"),
    "correction": ("correction__icontains", "str"),
    "tag": ("tag__in", "list")
}


def form_query(query, fields):
    values = {}
    if not isinstance(query, dict):
        query = dict(query)
    for param in query:
        if param in fields and query[param][0]:
            if fields[param][1] == 'str':
                values[fields[param][0]] = query[param][0]
            else:
                values[fields[param][0]] = query[param]
    return values
    
    
def exact_search(text):
    return Sentence.objects.filter(sentence__icontains = text)
    
 
def structure_word_query(query_dict):
    query_by_word = defaultdict(dict)
    for k, v in query_dict:
        if v[0]:
            print(k,v)
            generic_key, n = k.rsplit('_', 1)
            query_by_word[int(n)][generic_key] = v
    final_query_by_word = []
    for k in query_by_word:
        if any(x in word_fields for x in query_by_word[k]):
            final_query_by_word.append(query_by_word[k])
    return final_query_by_word
    
    
def get_word_results(query):
    values = form_query(query, word_fields)
    print('VALUES', values)
    results = Word.objects.filter(**values)
    return results
    
 
def check_distance(collected_results, curr_results, idx, query):
    distance_from, distance_to = int(query['distance_from'][0]), int(query['distance_to'][0])
    for result in curr_results:
        curr_sent = result.sentence.pk
        for i,curr_res in enumerate(collected_results):
            if curr_res[-1].sentence.pk == curr_sent:
                distance = result.pk - curr_res[-1].pk
                if distance >= distance_from and distance <= distance_to:
                    collected_results[i].append(result)
    collected_results = [x for x in collected_results if len(x) == idx+1]
    return collected_results
    
   
def search_detailed(query):
    structured_query = structure_word_query(query)
    print(structured_query)
    first_word_results = get_word_results(structured_query[0])
    sentences = {x.sentence.pk for x in first_word_results}
    results = [[x] for x in first_word_results]
    for i in range(1, len(structured_query)):
        if sentences:
            structured_query[i]['sentences'] = sentences
            word_results = get_word_results(structured_query[i])
            sentences &= {x.sentence.pk for x in word_results}
            results = check_distance(results, word_results, i, structured_query[i])
        else:
            results = []
    return results
    
    
def get_mistake_results(query):
    values = form_query(query, mistake_fields)
    print(values)
    results = Mistake.objects.filter(**values)
    return results
