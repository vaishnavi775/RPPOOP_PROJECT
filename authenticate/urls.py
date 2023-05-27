from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('Homepage/', views.Homepage_view, name='Homepage'),
    # path('Main/', views.main_view, name='main')
]