from django.shortcuts import render, redirect, get_object_or_404
from self.models import Article, Comment, Likes
from self.forms import ArticleForm
from django.contrib import messages
from django.http import JsonResponse
from account.models import User



def selfpg(request):  
    '''
    render the self page
    '''      
    return render(request, 'self/self.html')

def articleCreate(request):
    '''
    Create a new article instance
    
        1. If method is GET, render an empty form
        2. If method is POST:
            * validate the form and display error message if form is invalid
            * else, save it to the model and redirect to the article page
    '''
    template = 'self/articleCreateUpdate.html'
    if request.method =='GET':
        return render(request, template, {'articleForm':ArticleForm()})
    
    # POST
    articleForm = ArticleForm(request.POST, request.FILES)
    if not articleForm.is_valid():
        return render(request, template, {'articleForm':ArticleForm()})
    
    formsave = articleForm.save(commit=False)
    formsave.user = request.user
    formsave.save()
    newarticle = Article.objects.all().order_by('-id')[0]
    Likes.objects.create(article=newarticle)    
    messages.success(request, '成功發文瞜')
    return redirect('main:main')


def articleRead(request, articleId):
    
    '''
    1. Get the article; redirect to the 404 page if not found
    2. Render the articleRead template with the article instance and its associated comments
    '''
    
    article = get_object_or_404(Article, id=articleId)
    like = Likes.objects.get(article=article)

    context = {
            'article' : article,
            'like' : like,
            'comments' : Comment.objects.filter(article=article),
            'total_like_query' : len(like.user.all())
            }
            
    return render(request, 'self/articleRead.html', context)

    
def articleUpdate(request, articleId):
    '''
    Update the article instance
        1. Get the article to update; redirect to 404 if not found
        2. If method is GET, render a bound form
        3. If method is POST,
            * validate the form and render a bound form if the form is invalid
            * else, save it to the model and redirect to the articleRead page
    '''

    article = get_object_or_404(Article, id=articleId)
    template = 'self/articleCreateUpdate.html'
    if request.method == 'GET':
        articleForm = ArticleForm(instance=article)
        return render(request, template, {'articleForm':articleForm})

    # POST
    articleForm = ArticleForm(request.POST, instance=article)
    if not articleForm.is_valid():
        return render(request, template, {'articleForm':articleForm})
    articleForm.save()
    messages.success(request, '修改成功')
    return redirect('main:main')
    
def articleDelete(request, articleId):
    '''
    Delete the instance;
        1. Render the article page if the method is GET
        2. Get the article to delete; redirect to 404 if not found
    '''
    if request.method=="GET":
        return redirect('main:main')
    
    #POST
    article = get_object_or_404(Article, id=articleId)
    article.delete()
    messages.success(request, '文章已刪除')
    return redirect('main:main')

def articleLike(request, articleId):
    '''
    Add the user to the 'likes' field:
        1. Get the article; redirect to 404 if not found
        2. If the user does not exist in the "likes" field, add him/her
        3. If the user has exist in the "likes" field, move him/her
        3.Finally, redirect the articleRead page
    '''
    
    article = get_object_or_404(Article, id=articleId)   
    like = Likes.objects.get(article=article)
     
    if request.user not in like.user.all():
        like.user.add(request.user)
        total_like_query = len(like.user.all()) 
        return JsonResponse({'total_like_query':total_like_query})
    if request.user in like.user.all():
        like.user.remove(request.user)
        total_like_query = len(like.user.all()) 
        return JsonResponse({'total_like_query':total_like_query})
    
    
def commentCreate(request, articleId):
    '''
    Create a comment for an article
    1. Get the comment from the HTML form
    2. Store it to database
    '''

    if request.method == 'GET':
        return articleRead(request, articleId)
    
    # POST
    comment = request.POST['comment']
    
    if comment:
        comment = comment.strip()
        article = get_object_or_404(Article, id=articleId)
        new = Comment.objects.create(article=article, user=request.user, content=comment)
        name_dict = {
            'comment': comment,
            'user' :request.user.fullName,
            'time' :new.pubdateTime.strftime("%Y-%m-%d ")        
                     }
        return JsonResponse(name_dict)
    if not comment:
        return redirect('self:articleRead', articleId=articleId)
    
def commentUpdate(request, commentId):
    '''
    1. Get the comment to update and article; redirect to 404 if not found
    2. IF it is a 'GET' request, return
    3. IF the comment's author is not the user, return
    4. If comment is empty, delete the comment, else update the comment
    '''
    
    commentToUpdate = get_object_or_404(Comment, id=commentId)
    article = get_object_or_404(Article, id=commentToUpdate.article.id)
    if request.method == 'GET':
        commentToUpdate = commentToUpdate.content
        dic = {"comment" : commentToUpdate}
        return JsonResponse(dic)
    # POST
    if commentToUpdate.user != request.user:
        messages.error(request, '無修改權限')
        return redirect('self:articleRead', articleId=article.id)
    
    comment = request.POST['comment']
    if not comment:
        commentToUpdate.delete()
    
    else:
        commentToUpdate.content = comment
        commentToUpdate.save()
        
    name_dict = {
            'comment': comment,
            'user' :request.user.fullName,
            
                     }
    return JsonResponse(name_dict)


def commentDelete(request, commentId):
    '''
    1. Get the comment to update and article; redirect to 404 if not found
    2. IF it is a 'GET' request, return
    3. IF the comment's author is not the user, return
    4. Delete the comment
    '''
    
    comment = get_object_or_404(Comment, id=commentId)
    article = get_object_or_404(Article, id=comment.article.id)
    if request.method == 'GET':
        return articleRead(request, article.id)
    
    # POST
    if comment.user != request.user:
        messages.error(request, '無修改權限')
        return redirect('self:articleRead', articleId=article.id)
    
    comment.delete()
    dict = {"delete":"已刪除"}
    return JsonResponse(dict)
    
    
    
def userPage(request, userId):
    articleuser = get_object_or_404(User, id=userId)
    fullName = articleuser.fullName
    context = {
       'articleuser':articleuser,
       'fullName': fullName
        }
    return render(request, 'self/userPage.html', context)