from django.urls import path
from user_auth import views
urlpatterns = [
    path('/login',views.LoginAPIView.as_view(),name='user_auth_login')
]