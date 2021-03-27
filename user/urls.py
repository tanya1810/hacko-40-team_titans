from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user/<int:pk>/resources/', views.user_profile_resources, name='user_profile'),
    path('user/<int:pk>/feeds/', views.user_profile_feeds, name='user_profile_feeds'),
]