from django.urls import path
from app import views

urlpatterns = [
    path('login/', views.user_login_view, name="login"),
    path('sign-up/', views.user_sign_up_view, name="signup"),
    path('profile/', views.user_profile_view, name="profile"),
    path('logout/', views.user_logout_view, name="logout"),
    path('change-password/', views.user_password_change, name="passchange"),
]
