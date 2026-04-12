from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Post Form Adding
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long")
        return title
    
    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        
        if content and len(content) < 10:
            self.add_error('content', 'Content must be at least 10 characters')
            
        return cleaned_data
    
# Comment Form Adding
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['commenter', 'text']
    
    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 3:
            raise forms.ValidationError('Comment is too short')
        return text

# Register User
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']        
