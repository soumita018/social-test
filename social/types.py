from main.models import *
import graphene
from graphene_django.types import DjangoObjectType



class UserType(DjangoObjectType):

    class Meta:
        model = User
        fields = '__all__'


class ProfileType(DjangoObjectType):

    class Meta:
        model = Profile
        fields = '__all__'


class PostType(DjangoObjectType):

    class Meta:
        model = Post
        fields = '__all__'


class CommentType(DjangoObjectType):

    class Meta:
        model = Comment
        fields = '__all__'


