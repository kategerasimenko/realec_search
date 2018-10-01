from django.contrib import admin

from .models import Word, Mistake, Sentence, Text

admin.site.register(Word)
admin.site.register(Mistake)
admin.site.register(Sentence)
admin.site.register(Text)