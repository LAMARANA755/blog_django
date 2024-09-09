from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):   
    titre = models.CharField(max_length=250)
    contenu = models.TextField()
    auteur = models.ForeignKey(User, on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='article_image', null=True, blank=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.titre 


class Comment(models.Model):
    content = models.TextField()
    created_add = models.DateField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.article.titre 

