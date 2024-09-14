from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
 
class CustomUserCreationForm(UserCreationForm):# registration form
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)  # User model

class PostForm(forms.ModelForm): #ModelForm for the Post model to handle the creation and updating of posts.
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }     