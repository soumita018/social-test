from social.models import *
import graphene
from graphene_django.types import DjangoObjectType



class UserType(DjangoObjectType):
    image_url=graphene.String()

    class Meta:
        model = User
        fields = '__all__'
    
    def  resolve_image_url(self,args):
        if self.image:
            return self.image.url
        return ""


class ProfileType(DjangoObjectType):

    class Meta:
        model = Profile
        fields = '__all__'


class PostType(DjangoObjectType):
    image_url=graphene.String()

    class Meta:
        model = Post
        fields = '__all__'

    def  resolve_image_url(self,args):
        if self.image:
            return self.image.url
        return ""



    


class CommentType(DjangoObjectType):

    class Meta:
        model = Comment
        fields = '__all__'


