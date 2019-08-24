from django.shortcuts import render
from social.models import Comment
# Create your views here.

def pehla(request):
    p = Comment.objects.all()
    return render(request,'index.html',{'p':p})