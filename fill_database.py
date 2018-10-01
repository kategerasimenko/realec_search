import time
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'realec_search.settings'

import django
django.setup()

from search_app.models import Word, Mistake, Sentence, Text
from django.db import transaction


table_names = {
    'texts': (1, Text),
    'sentences': (2, Sentence),
    'mistakes': (3, Mistake),
    'words': (4, Word)
    }

m2m = {
    'words': 'mistake'
}


@transaction.atomic
def fill_database(data):
    for table_name in sorted(table_names, key=lambda x: table_names[x][0]):
        for row in data[table_name]:
            m2m_value = None
            if table_name in m2m:
                m2m_value = row.pop(m2m[table_name])
            st_int = time.time()
            obj = table_names[table_name][1](**row)
            if m2m_value is not None:
                obj.save()
                getattr(obj,m2m[table_name]).add(*m2m_value)
            obj.save()


fill_database({'texts':
                   [{'pk': 2,
                    'path': 'new/path/to/text',
                    'department': 'compsci',
                    'type': 'graph_description',
                    'mark': 55
                    }],
               'sentences':[{
                   'pk': 2,
                   'sentence': 'this is a new sentence that is diferent',
                   'text_id': 2}],
               'mistakes':[{
                   'pk': 3,
                   'text': 'that',
                   'correction': 'which',
                   'tag': 'complementizer',
                   'start_idx': 17,
                   'sentence_id': 2},{
                   'pk': 4,
                   'text': 'is diferent',
                   'correction': 'is different',
                   'tag': 'spelling',
                   'start_idx': 22,
                   'sentence_id': 2}],
               'words': [{
                   'pk': 4,
                   'pos': 'VBP',
                   'lemma': 'be',
                   'wordform': 'is',
                   'start_idx': 22,
                   'mistake': [4,2],
                   'sentence_id': 2},{
                   'pk': 3,
                   'pos': 'C',
                   'lemma': 'that',
                   'wordform': 'that',
                   'start_idx': 17,
                   'mistake': [3],
                   'sentence_id': 2}, {
                   'pk': 5,
                   'pos': 'ADJ',
                   'lemma': 'diferent',
                   'wordform': 'diferent',
                   'start_idx': 25,
                   'mistake': [4],
                   'sentence_id': 2}]})
        
