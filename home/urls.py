from django.urls import path

from home import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('connect/<operation>/<pk>/', views.change_friends, name='change_friends'),
]
