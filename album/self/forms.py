from django import forms
from self.models import Article, Likes



class ArticleForm(forms.ModelForm): 
    picture = forms.ImageField(label="照片")
    content = forms.CharField(label='故事', widget=forms.Textarea)
    
    class Meta:
        model = Article
        fields = ['picture', 'content']
    
   