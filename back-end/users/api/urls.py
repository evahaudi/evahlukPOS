from django.urls import path
from .views import ChefSignupView, ManagerSignupView, WaiterSignupView, CustomAuthToken, LogoutView, ManagerOnlyView, WaiterOnlyView, ChefOnlyView


urlpatterns = [
    path('signup/chef/',ChefSignupView.as_view()),
    path('signup/manager/',ManagerSignupView.as_view()),
    path('signup/waiter/',WaiterSignupView.as_view()),
    path('login/',CustomAuthToken.as_view(), name='auth-token'),
    path('logout/',LogoutView.as_view()),
    path('signup/chef/dashboard/',ChefOnlyView.as_view()),
    path('signup/manager/dashboard/',ManagerOnlyView.as_view()),
    path('signup/waiter/dashboard/',WaiterOnlyView.as_view()),
]


