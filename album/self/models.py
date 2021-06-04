from django.db import models
from account.models import User



class Article (models.Model):
    content = models.TextField()
    picture = models.ImageField(upload_to='image/')
    pubdateTime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.content
    
    
    class Meta:
        ordering = ['-pubdateTime']
    
    

class Comment (models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=128)
    pubdateTime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
     
    def __str__(self):
        return  self.content
    
    
    class Meta:
        ordering = ['pubdateTime']
        

class Likes (models.Model):
    user = models.ManyToManyField(User)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    
    def __str__(self):
        return  str(self.article)