from django.shortcuts import render,redirect
from .form import LoginForm
from .slides import SearchSlide
from .comments import Comment
from .models import RecycleCenter,Region

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

def search_slide_view(request):
    actor = request.POST.get('actor')
    member_ID = request.POST.get("ID")
    slide_word = request.POST.get("slide_word")
    searching_slides = SearchSlide()
    if request.method == "POST" and slide_word == "":
        slide_type = request.POST.get('slide_type')
        related_slides = searching_slides.search_slidetype(slide_type) #search type of slide
    else:
        related_slides = searching_slides.search_slidetitle(slide_word) #search existing word in title
    
    if related_slides.exists():
        found_message = "Here is the result "
    else:
        found_message = "doesn't found any result"
    
    return render(request, 'pages/SearchedSlide.html', context={
       "actor":actor,
       "member_ID":member_ID,
       "found_message":found_message,
       "related_slides":related_slides
    })

def selected_slide_view(request):
    actor = request.POST.get('actor')
    member_ID = request.POST.get("ID")
    slideID = request.POST.get("slideID")
    findslide = SearchSlide()
    slide = findslide.get_slide(slideID)
    comment = request.POST.get("comment")
    comments = Comment()
    if comment != None:
        comments.save_comment(comment,slideID,member_ID)
    comments = comments.get_related_comment(slideID)
    return render(request, 'pages/SelectedSlide.html', context={
       "actor":actor,
       "member_ID":member_ID,
       "slide":slide,
       "comments":comments
    })

def RC_view(request):
    actor = request.GET.get('actor')
    member_ID = request.GET.get("ID")
    return render(request, 'pages/RecycleCenter.html', context={
       "actor":actor,
       "member_ID":member_ID,
    })

def search_RC_view(request):
    actor = request.POST.get('actor')
    member_ID = request.POST.get("ID")
    searchregion = request.POST.get("region")
    searchregion=searchregion.lower()
    searchregion=searchregion.replace(" ", "")
    
    recycle_centers_qs = list(RecycleCenter.objects.filter(rc_region=searchregion))
    # Convert queryset to list of dictionaries
    recycle_centers = [
        {
            "rc_name": rc.rc_name,
            "rc_latitude": rc.rc_latitude,
            "rc_longitude": rc.rc_longitude,
            "rc_address": rc.rc_address,
            "rc_ID": rc.rc_ID
        }
        for rc in recycle_centers_qs
    ]

    region_obj = Region.objects.get(region=searchregion)
    region = {
        "region": region_obj.region,
        "region_latitude": region_obj.region_latitude,
        "region_longitude": region_obj.region_longitude,
    }
    return render(request, 'pages/SearchRecycleCenter.html', context={
       "actor":actor,
       "member_ID":member_ID,
       "recycle_centers":recycle_centers,
       "region":region
    })

def notification_view(request):
    actor = request.GET.get('actor')
    member_ID = request.GET.get("ID")
    return render(request, 'pages/Notification.html', context={
       "actor":actor,
       "member_ID":member_ID
    })