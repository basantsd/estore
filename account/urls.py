from django.urls import path
from .views import LoginView,RegisterView,LogoutView,ProfileView,AccountAcivateView

urlpatterns = [
    path('login/',LoginView.as_view(),name="login"),
    path("register/",RegisterView.as_view(),name="register"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("profile/",ProfileView.as_view(),name="profile"),
    path("activate/<token>/",AccountAcivateView.as_view(),name="activate")
]
