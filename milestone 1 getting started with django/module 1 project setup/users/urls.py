from django.urls import path
from users.views import sign_up, sign_in, user_logout

app_name = "users"

urlpatterns = [
    path("sign-up/", sign_up, name="sign-up"),
    path("login/",sign_in, name="login"),
    path("logout/",user_logout, name="logout")
]