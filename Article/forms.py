from django.forms import ModelForm
from .models import *

class ArticleForm(ModelForm):
        class Meta:
            model = Article
            fields = ['titre','contenu', 'auteur', 'image']
            
            
            
            
            