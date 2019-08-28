from social.types import UserType,ProfileType,PostType,CommentType
from social.models import User,Profile,Post,Comment
import graphene
from graphene import ObjectType, String,Field

class Login(ObjectType):
    id=String()
    name = String()

class Query(object):
    profile = graphene.List(ProfileType,id=graphene.ID())
    posts = graphene.List(PostType)
    post = graphene.List(PostType,id=graphene.ID())
    comments = graphene.List(CommentType)
    user = graphene.List(UserType,search=graphene.String())
    login = Field(Login,phone=graphene.String(),password=graphene.String())

    def resolve_post(self,info,id=None):
        # print(dir(graphene))
        # print('c')
        if id is not None:
            return Post.objects.filter(id=id)
        return Post.objects.all()

    def resolve_posts(self,info,**kwargs):
        return Post.objects.all()

    def resolve_commets(self,info,**kwargs):
        return Comment.objects.all()

    def resolve_user(self,info,search=None):
        if search is not None:
            return User.objects.filter(name__icontains=search)
        return User.objects.all()
        
    def resolve_profile(self,info,id=None):
        if id is not None:
          return Profile.objects.filter(user__id=id)
        return Profile.objects.all()

    def resolve_login(self,info,phone=None,password=None):
        if phone and password is not None:
            user = User.objects.get(phone=phone)
            print(user)
            print(user.check_password(password))
            if user.check_password(password):
                print("idhar",user.id)
                return {'id':user.id,'name':user.name} 
            raise("error")      