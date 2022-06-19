from django import forms
from .models import Article, Comment

# Create your models here.

class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'my-title form-control'}))
    description = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class': 'my-description form-control'}))

    class Meta:
        model = Article
        #fields = '__all__'
        exclude = ('user',)

class CommentForm(forms.ModelForm):
    content = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'my-content form-control'}))
    
    class Meta:
        model = Comment
        fields = ('content',)