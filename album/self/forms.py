from django import forms
from self.models import Article, Likes



class ArticleForm(forms.ModelForm): 
    picture = forms.ImageField(label="η§η")
    content = forms.CharField(label='ζδΊ', widget=forms.Textarea)
    
    class Meta:
        model = Article
        fields = ['picture', 'content']
    
   