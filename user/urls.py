from django.urls import path
from user.views import CreateUserView, ManageUserView, EmployeeListView, EmployeeDetailView, CreateEmployeeView, CreateVoteView, VoteListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = "user"

urlpatterns = [
    # User-related views (v1)
    path("v1/register/", CreateUserView.as_view(), name="register"),
    path("v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("v1/me/", ManageUserView.as_view(), name="manage_user"),

    # Employee-related views (v1)
    path("v1/employee/", CreateEmployeeView.as_view(), name="create_employee"),
    path("v1/employee/list/", EmployeeListView.as_view(), name="employee_list"),
    path("v1/employee/<int:pk>/", EmployeeDetailView.as_view(), name="employee_detail"),

    # Vote-related views (v1)
    path("v1/vote/", CreateVoteView.as_view(), name="create_vote"),
    path("v1/vote/list/", VoteListView.as_view(), name="vote_list"),

    # User-related views (v2)
    path("v2/register/", CreateUserView.as_view(), name="register"),
    path("v2/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("v2/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("v2/me/", ManageUserView.as_view(), name="manage_user"),

    # Employee-related views (v2)
    path("v2/employee/", CreateEmployeeView.as_view(), name="create_employee"),
    path("v2/employee/list/", EmployeeListView.as_view(), name="employee_list"),
    path("v2/employee/<int:pk>/", EmployeeDetailView.as_view(), name="employee_detail"),

    # Vote-related views (v2)
    path("v2/vote/", CreateVoteView.as_view(), name="create_vote"),
    path("v2/vote/list/", VoteListView.as_view(), name="vote_list"),
]
