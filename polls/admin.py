from django.contrib import admin
from .models import Post, Choice
from .models import Question
from .models import Kazakh

admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Kazakh)
admin.site.register(Choice)

