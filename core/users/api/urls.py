from django.urls import path
from .views import ChefSignupView, ManagerSignupView, WaiterSignupView


urlpatterns = [
    path('signup/chef/',ChefSignupView.as_view()),
    path('signup/manager/',ManagerSignupView.as_view()),
    path('signup/waiter/',WaiterSignupView.as_view()),
]

