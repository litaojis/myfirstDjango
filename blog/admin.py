from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
#Register your models here.

admin.site.register(Article,ArticleAdmin)
admin.site.register(Person,PersonAdmin)
admin.site.register(Tag)
admin.site.register(Author)
