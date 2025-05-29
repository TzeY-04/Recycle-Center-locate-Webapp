from django.urls import path
from . import views

#Define url pattern
urlpatterns = [
    path('', views.login_view, name="login"),
    path('home',views.home_view, name="home"),
    path('slide',views.slide_view, name="slide"),
    path('RecycleCenter',views.RC_view, name="RecycleCenter"),
]