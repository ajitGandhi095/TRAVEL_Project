from django.shortcuts import render
from App1.forms import SignUpForm
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    return render(request, "App1/index.html")

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

def signup(request):

    form= SignUpForm()

    if request.method == "POST":
        form= SignUpForm(request.POST)
        if form.is_valid():
            user= form.save()
            user.set_password(user.password)
            user.save()
            print("SignUp SuccessFully")
            return HttpResponseRedirect('/accounts/login')

    my_dict= {"form":form}
    return render(request, 'App1/signup.html', my_dict)

def homepage(request):
    return render(request, 'App1/home.html')
