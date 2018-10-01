from django.db import models


class Text(models.Model):
    path = models.TextField()
    department = models.CharField(max_length=500)
    type = models.CharField(max_length=20, choices=[('graph_description','graph description'),
                                                    ('opinion_essay','opinion essay')])
    mark = models.IntegerField()
 
 
class Sentence(models.Model):
    sentence = models.CharField(max_length=1000)
    text = models.ForeignKey('Text', on_delete=models.CASCADE)

 
class Mistake(models.Model):
    text = models.CharField(max_length=500)
    tag = models.CharField(max_length=100)
    correction = models.CharField(max_length=500)
    start_idx = models.IntegerField()
    weight_language = models.CharField(max_length=10, blank=True, null=True,
                                       choices=[('Minor','Minor'),('Major','Major'),('Critical','Critical')])
    weight_understanding = models.CharField(max_length=10, blank=True, null=True,
                                            choices=[('Minor','Minor'),('Major','Major'),('Critical','Critical')])
    delete = models.BooleanField(default=False)
    cause = models.CharField(max_length=30, blank=True, null=True,
                             choices=[('Typo','Typo'),('L1_interference','L1 interference'),
                                      ('Absence_of_Category_in_L1','Absence of Category in L1'), ('Other','Other')])
    sentence = models.ForeignKey('Sentence', on_delete=models.CASCADE)
 

class Word(models.Model):
    pos = models.CharField(max_length=10)
    lemma = models.CharField(max_length=100)
    wordform = models.CharField(max_length=100)
    start_idx = models.IntegerField()
    mistake = models.ManyToManyField('Mistake')
    sentence = models.ForeignKey('Sentence', on_delete=models.CASCADE)


