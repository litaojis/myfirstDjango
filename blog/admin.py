from django.contrib import admin
from .models import Article,Tag,Author

# Register your models here.

admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Author)

