from django.shortcuts import render
from self.models import Article, Comment, Likes
from django.db.models.query_utils import Q

def main(request):  
    '''
    render the main page
    '''
    articles = {article:Comment.objects.filter(article=article)[:2] for article in Article.objects.all()}
    
    context = {'articles':articles}
    
    return render(request, 'main/main.html', context)

def articleSearch(request):
    '''
    Search for articles:
        1. Get the "searchTerm" from the HTML form
        2. Use "searchTerm" for filtering
    '''
    searchTerm = request.GET.get('searchTerm')
    articles = {article:Comment.objects.filter(article=article)[:2] for article in Article.objects.filter(Q(content__icontains=searchTerm))}
    
    context = {'articles':articles,'searchTerm':searchTerm }
    return render(request, 'main/articleSearch.html', context)