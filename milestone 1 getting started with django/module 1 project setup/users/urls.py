from django.urls import path
from users.views import sign_up, sign_in, user_logout, active_user, admin_dashboard, assign_role, create_group, group_list, CustomLoginView, ProfileView

app_name = "users"

urlpatterns = [
    path("sign-up/", sign_up, name="sign-up"),
    # path("login/",sign_in, name="login"),
    path("login/",CustomLoginView.as_view(), name="login"),
    path("logout/",user_logout, name="logout"),
    path("activate/<int:user_id>/<str:token>/",active_user),
    path("admin/dashboard/", admin_dashboard, name="admin-dashboard"),
    path("admin/<int:user_id>/assign-role/",assign_role, name="assign-role"),
    path("admin/create-group/", create_group, name="create-group"),
    path("admin/group-list/",group_list, name="group-list"),
    path("profile/", ProfileView.as_view(), name="profile")
]