from django.contrib import admin
from django import forms
from .models import User, Profile, Post, Comment

class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'


class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
    list_display = ['name', 'phone', 'email', 'is_active', 'is_admin', 'is_staff']

admin.site.register(User, UserAdmin)


class ProfileAdminForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    list_display = ['about']

admin.site.register(Profile, ProfileAdmin)


class PostAdminForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['post_text', 'image', 'posted_time']

admin.site.register(Post, PostAdmin)


class CommentAdminForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'


class CommentAdmin(admin.ModelAdmin):
    form = CommentAdminForm
    list_display = ['comment', 'posted_time']

admin.site.register(Comment, CommentAdmin)


