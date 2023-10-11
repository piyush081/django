from django.urls import path
from app import views
from .views import login_view


urlpatterns = [
    path('hello/',views.home),
    path('',views.index,name='index'),
    path('login/', login_view, name='login')
]