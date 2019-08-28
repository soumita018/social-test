from graphene_django.forms.mutation import DjangoModelFormMutation
from social.types import UserType,ProfileType,PostType,CommentType
from social.models import User,Profile,Post,Comment
from social.forms import UserForm,ProfileForm,PostForm,CommentForm
from graphene import Field,AbstractType,String,ID,Boolean,Mutation



class PostMutation(DjangoModelFormMutation):
    post = Field(PostType)

    # @classmethod
    # def perform_mutate(cls, form, info):
    #     post_obj = form.save()
    #     try:
    #         image = info.context.FILES['file']
    #         blog_obj.image = image
    #         blog_obj.save()
    #         kwargs = {cls._meta.return_field_name: blog_obj}
    #         return cls(errors=[], **kwargs)
    #     except:
    #         kwargs = {cls._meta.return_field_name: blog_obj}
    #         return cls(errors=[], **kwargs)

    class Meta:
        form_class = PostForm


class CommentMutation(DjangoModelFormMutation):
    comment = Field(CommentType)

    class Meta:
        form_class = CommentForm


class ProfileMutation(DjangoModelFormMutation):
    profile = Field(ProfileType)

    class Meta:
        form_class = ProfileForm


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

class Mutation(AbstractType):
    create_post = PostMutation.Field()
    create_comment = CommentMutation.Field()
    create_profile = ProfileMutation.Field()
    create_user = UserMutation.Field()
    add_friend = AddFriend.Field()