from django.urls import path
from .views import *
app_name = 'article'
urlpatterns = [
    path('',index, name='index'),
    path('ajout_article',ajout_article, name='ajout_article'),
    path('modifier_article/<int:id>',modifier_article, name='modifier_article'),
    path('supprimer_article/<int:id>',supprimer_article, name='supprimer_article'),
    path('detail_article/<int:id>',detail_article, name='detail_article'),


]
