from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

# Create your models here.

class Articleseries(models.Model):
    title= models.CharField(max_length=200)
    subtitle=models.CharField(max_length=200, blank=True,default="")
    slug=models.SlugField("Series Slug",unique=True,null=False,blank=False)
    published=models.DateTimeField('date published',default=timezone.now)
    
    class meta:
        verbose_name_plural ="Series"
        ordering =['-published']


class Article(models.Model):
    title= models.CharField(max_length=200)
    subtitle=models.CharField(max_length=200, blank=True,default="")
    article_slug=models.SlugField("Series Slug",unique=True,null=False,blank=False)
    content = HTMLField(blank=True, default="")
    notes = HTMLField(blank=True, default="")
    published=models.DateTimeField('date published',default=timezone.now)
    modified=models.DateTimeField('date published',default=timezone.now)
    series=models.ForeignKey(Articleseries, on_delete=models.SET_DEFAULT, verbose_name="Series",default="",)

    def __str__(self):
        return self.title
    @property
    def slug(self):
        return self.article_slug
    
    class meta:
        verbose_name_plural ="Series"
        ordering =['-published']


