from django.urls import path
from . import views

#Define url pattern
urlpatterns = [
    path('', views.login_view, name="login"),
    path('home',views.home_view, name="home"),
    path('slide',views.slide_view, name="slide"),
    path('RecycleCenter',views.RC_view, name="RecycleCenter"),
    path('SearchedSlide',views.search_slide_view, name="SearchedSlide"),
    path('SelectedSlide',views.selected_slide_view, name="SelectedSlide"),
    path('Notification',views.notification_view, name="Notification"),
    path('SearchRecycleCenter',views.search_RC_view, name="SearchRecycleCenter"),
    path('NewFoundRecycleCenter',views.new_RC_found, name="NewFoundRecycleCenter"),
    path('NewFoundForm',views.new_RC_form, name="NewFoundForm"),
]