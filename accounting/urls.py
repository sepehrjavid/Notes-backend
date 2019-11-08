from django.urls import path

from accounting.views import UserSignUpView, UserRetrieveView, UserPasswordChangeView

app_name = "accounting"

urlpatterns = [
    path('signup', UserSignUpView.as_view()),
    path('retrieve', UserRetrieveView.as_view()),
    path('passwordChange', UserPasswordChangeView.as_view()),
]
