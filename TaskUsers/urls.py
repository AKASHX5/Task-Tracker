from django.urls import path

from .views import SignUpView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [

    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('log_in/', LoginView.as_view(), name='log_in'),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]