from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.

def article_list (request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles.html', {'articles':articles})

def article_id (request, id):
    article = Article.objects.filter(id=id) 
    return render(request, 'articles/articles.html', {'articles':article})
 
