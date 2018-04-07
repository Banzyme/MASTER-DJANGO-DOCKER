from django.shortcuts import render

# Create your views here.
app_name = 'twistapp'
title = 'Twisted | Home page'
def home(request):
    context = {'title':title, 'app_name':app_name}

    return render(request, (app_name+'/home.html'), context)

def home_2(request):

    context = {'title':title, 'app_name':app_name}

    return render(request, (app_name+'/home_2.html'), context)

def home_3(request):
    context = {'title':title, 'app_name':app_name}

    return render(request, (app_name+'/home_3.html'), context)