from graphene_django.forms.mutation import DjangoModelFormMutation
from main.types import UserType,ProfileType,PostType,CommentType
from main.models import User,Profile,Post,Comment
from main.forms import UserForm,ProfileForm,PostForm,CommentForm
from graphene import Field,AbstractType,String,ID,Boolean,Mutation,List



class PostMutation(DjangoModelFormMutation):
    post = Field(PostType)

    @classmethod
    def perform_mutate(cls, form, info):
        post_obj = form.save()
        try:
            image = info.context.FILES['file']
            post_obj.image = image
            post_obj.save()
            kwargs = {cls._meta.return_field_name: post_obj}
            return cls(errors=[], **kwargs)
        except:
            kwargs = {cls._meta.return_field_name: post_obj}
            return cls(errors=[], **kwargs)

    class Meta:
        form_class = PostForm


class CommentMutation(DjangoModelFormMutation):
    comment = Field(CommentType)

    class Meta:
        form_class = CommentForm


# class ProfileMutation(DjangoModelFormMutation):
#     profile = Field(ProfileType)

#     class Meta:
#         form_class = ProfileForm


class UserMutation(DjangoModelFormMutation):
    user = Field(UserType)

    @classmethod
    def perform_mutate(cls, form, info):
        obj = form.save()
        obj.set_password(form.cleaned_data['password'])
        obj.save()
        kwargs = {cls._meta.return_field_name: obj}
        return cls(errors=[], **kwargs)


    class Meta:
        form_class = UserForm


class AddFriend(Mutation):
    okay = Boolean()

    class Arguments:
        my_id = ID(required=True)
        friend_id = ID(required=True)
        unfriend = Boolean(required=True)

    def mutate(self, info, my_id,friend_id, unfriend):
        user = User.objects.get(id=my_id)
        user_friend = User.objects.get(id=friend_id)
        profile = Profile.objects.get(id=user.id)
        profile_friend = Profile.objects.get(id=user_friend.id)
        if unfriend:
            profile.friends.remove(user_friend)
            profile_friend.friends.remove(user)
        else:
            profile.friends.add(user_friend)
            profile_friend.friends.add(user)

        return AddFriend(okay=True)


class ProfileMutation(Mutation):
    # user = ID()
    profile = Field(ProfileType)
    # friends = List()
    # about = String()
    # city = String()
    # name = String()
    # phone = String()
    # image = String()

    class Arguments:
        id = ID()
        about = String()
        city = String()
        name = String()
        phone = String()
        email=String(required=True)
        

    def mutate(self, info, id,about, city,email,name,phone):
        user_obj = User.objects.get(id=id)
        profile = Profile.objects.get(id=id)
        try:
            image=info.context.FILES['file']
            user_obj.image=image
        except:
            pass
        user_obj.email=email
        user_obj.name=name
        user_obj.phone=phone
        user_obj.save()
        profile.about=about
        profile.city=city
        profile.save()
        return ProfileMutation(profile=profile)



# class ProfileMutation(Mutation):
#     okay = Boolean()

#     class Arguments:
#         my_id = ID(required=True)
#         friend_id = ID(required=True)
#         unfriend = Boolean(required=True)

#     def mutate(self, info, my_id,friend_id, unfriend):
#         user = User.objects.get(id=my_id)
#         user_friend = User.objects.get(id=friend_id)
#         profile = Profile.objects.get(id=user.id)
#         profile_friend = Profile.objects.get(id=user_friend.id)
#         if unfriend:
#             profile.friends.remove(user_friend)
#             profile_friend.friends.remove(user)
#         else:
#             profile.friends.add(user_friend)
#             profile_friend.friends.add(user)

#         return AddFriend(okay=True)

class Mutation(AbstractType):
    create_post = PostMutation.Field()
    create_comment = CommentMutation.Field()
    create_profile = ProfileMutation.Field()
    create_user = UserMutation.Field()
    add_friend = AddFriend.Field()