from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def index(request):
    article = Article.objects.all().order_by('-id')
    context = {
        'articles': article
    }
    template_name = 'article/article.html'
    
    return render(request, f'{template_name}', context)

def ajout_article(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('article:index')
    else:
        form = ArticleForm()
    context = {
        'form': form
    }

    template_name = 'article/ajout_article.html'
    
    return render(request, f'{template_name}', context)


def modifier_article(request, id):
    article = Article.objects.get(id=id)
    if request.POST:
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article:index')
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form
    }

    template_name = 'article/ajout_article.html'
    
    return render(request, f'{template_name}', context)


def supprimer_article(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('article:index')


def detail_article(request, id):
    article = Article.objects.get(id=id)
    context = {
        'article': article
    }
    template_name = 'article/detail_article.html'
    
    return render(request, f'{template_name}', context)


