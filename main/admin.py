from django.contrib import admin
from .models import Article, Articleseries

# Register your models here.
 


class ArticleSeriesAdmin(admin.ModelAdmin):
    fields = ['title' ,'subtitle' ,'slug' ,'published' ]

class ArticlesAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Header", {'fields': ["title", "subtitle", "article_slug", "series"]}),
        ("Content", {"fields": ["content", "notes"]}),
        ("Date", {"fields": ["modified"]})
    ]

admin.site.register(Articleseries, ArticleSeriesAdmin)
admin.site.register(Article,ArticlesAdmin)