from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post,Tag
from .models import Comment
from taggit.forms import TagWidget




class CustomUserCreationForm(UserCreationForm):# registration form
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        
        def save(self, commit=True):
         user = super().save(commit=False)
         user.email = self.cleaned_data['email']
         if commit:
            user.save()
            return user

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)  # User model

class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),  # Use TagWidget for tags
        }
