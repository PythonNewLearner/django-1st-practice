from django.shortcuts import render
from django2_app.models import User


# Create your views here.

def index(request):
    return render(request,'django2_app/index.html')


def users(request):
    users_list = User.objects.order_by('first_name')
    user_dict ={'users':users_list}
    return render(request,'django2_app/user.html',context=user_dict)