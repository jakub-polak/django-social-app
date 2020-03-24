from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts import views

urlpatterns = [
    path('', views.home),
    path('login/', LoginView.as_view(template_name='accounts/login.html')),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html')),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile, name='profile'),
]
