from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.response import get_template
from django.http.response import Context
from django.shortcuts import render_to_response
from article.models import Article, Comments
        
def template_simple(request):
  view = "template_three"
  return render_to_response('myview.html', {'name': view})
            
def articles(request):
  return render_to_response('article.html', {'articles': Article.objects.all()})
            
def article(request, article_id=1)
  return render_to_response('article.html', {'article': Article.objects.get(id=article_id),
                                      'comments': Comments.objects.filter(comments_article_id=article_id)})
