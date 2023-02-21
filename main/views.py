from django.shortcuts import render
from .models import Article,Articleseries
from django .http import HttpResponse
# Create your views here.



def homepage(request):
    matching_series = Articleseries.objects.all()

    return render(request=request,
                  template_name="main/home.html",
                context={'objects':matching_series}
    )

def series(request,series:str):
    matching_series= Article.objects.filter(series__slug=series).all()

    return render(
        request=request,
        template_name="main/home.html",
        context={'objects':matching_series}
    )

def article(request,series:str ,article: str):
    matching_article= Article.objects.filter(series__slug=series ,Article_slug=Article).first()


    return render(
                request=request,
                template_name="main/article.html",
                context={'object':matching_article}
    )




def index(request):

    return render(request, 'main/index.html')





 