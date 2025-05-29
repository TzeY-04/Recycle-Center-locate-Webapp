from django.shortcuts import render,redirect
from .form import LoginForm

# Create your views here.

def login_view(request): 
    error_message = ""
    actor = "guest"
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        ID = request.POST.get('ID')
        password = request.POST.get('password')
        if login_form.verify_Member(ID,password):
            actor = "member"
            return render(request, 'pages/home.html', context={
                "member_ID" : login_form.ID,
                "actor" : actor 
            })
        else:
            error_message = "ID or Password Incorrect"
    else:
        login_form = LoginForm()
    return render(request, 'pages/login.html', context={
        "form" : login_form,
        "error_message" : error_message,
        "actor" : actor
    })

def home_view(request):
    actor = request.GET.get('actor')
    member_ID = request.GET.get("ID")
    return render(request, 'pages/home.html', context={
       "actor":actor,
       "member_ID":member_ID
    })

def slide_view(request):
    actor = request.GET.get('actor')
    member_ID = request.GET.get("ID")
    return render(request, 'pages/slide.html', context={
       "actor":actor,
       "member_ID":member_ID
    })

def RC_view(request):
    actor = request.GET.get('actor')
    member_ID = request.GET.get("ID")
    return render(request, 'pages/RecycleCenter.html', context={
       "actor":actor,
       "member_ID":member_ID
    })