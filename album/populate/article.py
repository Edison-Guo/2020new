from populate import base
from self.models import Article, Comment


images = ['image/img1.jpg', 'image/img2.jpg', 'image/img3.jpg', 'image/img4.jpg', 'image/img5.jpg']
comments = ['講得真爛', '這個不錯喔', '請問可以分享嗎', '太厲害了']


def populate():
    print('Populating articles and comments ...', end='')
    Article.objects.all().delete()
    Comment.objects.all().delete()
    
    for image in images:
        article = Article()
        article.picture = image
        for j in range(5):
            article.content += image + '\n'
        article.save()
        for comment in comments:
            Comment.objects.create(article=article, content=comment)
    
    print('done')
    
    
if __name__ =='__main__':
    populate()
