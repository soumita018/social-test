from django import forms
from social.models import User, Profile, Post, Comment


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("name","email","password","phone","id")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
