from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("signup/", views.signup_view, name="signup_view" ),
    # path("login/", views.CustomLoginView.as_view(), name="login_view"),
    path("login/", views.login_view, name="login_view"),
    path("logout/", LogoutView.as_view(), name="logout_view"),
]

