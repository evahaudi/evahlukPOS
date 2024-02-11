from django.urls import path
from .views import ChefSignupView, user_logout, ManagerSignupView, WaiterSignupView, CustomAuthToken, ManagerOnlyView, WaiterOnlyView, ChefOnlyView, GetUserByUsernameView, UpdateUserByUsername, DeleteUserByUsername


urlpatterns = [
    path('signup/chef/',ChefSignupView.as_view()),
    path('logout/', user_logout, name='logout'),
    path('signup/manager/',ManagerSignupView.as_view()),
    path('signup/waiter/',WaiterSignupView.as_view()),
    path('login/',CustomAuthToken.as_view(), name='auth-token'),
    path('signup/chef/dashboard/',ChefOnlyView.as_view()),
    path('signup/manager/dashboard/',ManagerOnlyView.as_view()),
    path('signup/waiter/dashboard/',WaiterOnlyView.as_view()),
    path('deleteuserbyusername/<str:username>/',DeleteUserByUsername.as_view(), name='delete_user_by_username'),
    path('updateuserbyusername/<str:username>/',UpdateUserByUsername.as_view(), name='update_user_by_username'),
    path('getuserbyusername/',GetUserByUsernameView.as_view(), name='get_user_by_username'),
]



