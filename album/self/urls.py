from django.urls import path
from self import views



app_name = 'self'
urlpatterns = [
    path('',views.selfpg, name='self' ),
    path('articleCreate/', views.articleCreate, name='articleCreate' ),
    path('articleUpdate/<int:articleId>', views.articleUpdate, name='articleUpdate' ),
    path('articleDelete/<int:articleId>', views.articleDelete, name='articleDelete' ),
    path('articleRead/<int:articleId>', views.articleRead, name='articleRead' ),
    path('articleLike/<int:articleId>', views.articleLike, name='articleLike' ),
    path('commentCreate/<int:articleId>', views.commentCreate, name='commentCreate' ),
    path('commentDelete/<int:commentId>', views.commentDelete, name='commentDelete' ),
    path('commentUpdate/<int:commentId>', views.commentUpdate, name='commentUpdate' ),
    path('userPage/<int:userId>', views.userPage, name='userPage' ),
    ]

