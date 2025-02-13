from django.urls import path
from user.views import CreateUserView, ManageUserView, EmployeeListView, EmployeeDetailView, CreateEmployeeView, CreateVoteView, VoteListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = "user"

urlpatterns = [
    # User-related views
    path("register/", CreateUserView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", ManageUserView.as_view(), name="manage_user"),

    # Employee-related views
    path("employee/", CreateEmployeeView.as_view(), name="create_employee"),
    path("employee/list/", EmployeeListView.as_view(), name="employee_list"),
    path("employee/<int:pk>/", EmployeeDetailView.as_view(), name="employee_detail"),

    # Vote-related views
    path("vote/", CreateVoteView.as_view(), name="create_vote"),
    path("vote/list/", VoteListView.as_view(), name="vote_list"),
]