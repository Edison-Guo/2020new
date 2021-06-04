from django.contrib import admin

from self.models import Article, Comment, Likes



class CommentAdmin(admin.ModelAdmin):
    list_display = ['article', 'content', 'pubdateTime']
    list_display_links = ['article']
    list_filter = ['article', 'content']
    search_fields = ['content']
    list_editable = ['content']
    
    
    class Meta:
        model = Comment



admin.site.register(Article)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Likes)
