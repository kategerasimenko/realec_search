from django import forms
from search_app.models import *


class ExactMatchForm(forms.Form):
    exact_query = forms.CharField(label='Word or phrase', max_length=500)
    
    
class WordSearchForm(forms.Form):
    wordform = forms.CharField(label='Wordform', max_length=100, required=False)
    lemma = forms.CharField(label='Lemma', max_length=100, required=False)
    pos_choices = sorted(Word.objects.values_list('pos',flat=True).distinct())
    pos = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=zip(*[pos_choices]*2), label='Part of speech', required=False)
    mistake_choices = sorted(Mistake.objects.values_list('tag',flat=True).distinct())
    mistake = forms.MultipleChoiceField(zip(*[mistake_choices]*2), label='Mistake tag', required=False) # load from json instead
    
    
class NextWordSearchForm(WordSearchForm):
    distance_from = forms.IntegerField(initial=1)
    distance_to = forms.IntegerField(initial=1)
    
    
class MistakeSearchForm(forms.Form):
    text = forms.CharField(label='Incorrect word or phrase', max_length=500)
    correction = forms.CharField(label='Word or phrase in a correction', max_length=500)
    mistake_choices = sorted(Mistake.objects.values_list('tag',flat=True).distinct())
    tag = forms.MultipleChoiceField(zip(*[mistake_choices]*2), label='Mistake tag', widget=forms.CheckboxSelectMultiple, required=False) # load from json instead