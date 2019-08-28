from django.db import models 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email,phone,name, password=None):  #
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not phone:
            raise ValueError('Users must have a phone number')

        if not name:
            raise ValueError('Users must have a name')

        
        user = self.model(
            email = self.normalize_email(email),
            phone = phone,
            name = name,
        )
        user.set_password(password)
        user.is_admin=False
        user.is_staff=False
        user.save(using=self._db)
        return user

    def create_superuser(self,email,phone,name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            phone=phone,
            name=name,
            password=password,
        )
        user.is_admin = True
        user.is_staff=True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    

    name = models.CharField(max_length=100,blank=True,null=True)
    phone_regex = RegexValidator(regex=r'^[0-9]{10}$', message="Phone number must be 10 digits and entered in the format: '9775876662'.")
    phone = models.CharField(validators=[phone_regex],blank=True,null=True, max_length=10,unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    image = models.ImageField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name','email']

    def __str__(self):
        return self.phone

class Profile(models.Model):
  
  user = models.OneToOneField(User,related_name='User',on_delete=models.CASCADE,blank=True,null=True)
  friends = models.ManyToManyField(User,related_name='Friends',blank=True)
  about = models.TextField(blank=True,null=True)
  city = models.CharField(max_length=100,blank=True,null=True)

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


#   def __str__(self):
#         return self.user.name

class Post(models.Model):
  
  posted_by = models.ForeignKey(User,related_name='posted_by',on_delete=models.CASCADE,blank=True,null=True)
  post_text = models.TextField(blank=True,null=True)
  image = models.ImageField(blank=True,null=True)
  posted_time = models.DateTimeField(auto_now_add=True,blank=True,null=True)

  def __str__(self):
        return self.posted_by.name

class Comment(models.Model):
  
  commented_by = models.ForeignKey(User,related_name='commented_by',on_delete=models.CASCADE,blank=True,null=True)
  post = models.ForeignKey(Post,related_name='post',on_delete=models.CASCADE,blank=True,null=True)
  comment = models.TextField(blank=True,null=True)
  posted_time = models.DateTimeField(auto_now_add=True,blank=True,null=True)

  def __str__(self):
        return self.commented_by.name


  

  

