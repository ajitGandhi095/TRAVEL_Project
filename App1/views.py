from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "App1/index.html")

def login(request):
    msg="Welcome to Travel Point"
    my_dict= {"msg":msg}

    return render(request, 'App1/login.html', my_dict)

def signup(request):
    msg="Welcome to Travel Point"
    my_dict= {"msg":msg}

    return render(request, 'App1/signup.html', my_dict)

def home1(request):
    return render(request, 'App1/index.html')

def about(request):
    msg="Welcome to Travel Point"
    my_dict= {"msg":msg}

    return render(request, 'App1/about.html', my_dict)

def offers(request):
    msg="Welcome to Travel Point"
    my_dict= {"msg":msg}

    return render(request, 'App1/offer.html', my_dict)

def package(request):
    msg="Welcome to Travel Point"
    my_dict= {"msg":msg}

    return render(request, 'App1/package.html', my_dict)

def contact(request):
    msg="Welcome to Travel Point"
    my_dict= {"msg":msg}
    
    return render(request, 'App1/contact.html', my_dict)

def homepage(request):
    return render(request, 'App1/home.html')
