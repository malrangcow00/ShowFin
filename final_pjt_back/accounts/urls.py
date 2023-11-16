from django.urls import path,include
from . import views
from .views import CustomRegisterView, CustomUserDetailsView, change_password
from dj_rest_auth.registration.views import RegisterView
from .serializer import CustomRegisterSerializer

app_name = 'accounts'
urlpatterns = [
    path('signup/', CustomRegisterView.as_view(), name='account_signup'),
    path('user/', CustomUserDetailsView.as_view(), name='account_userinfo'),
    path('user_info/', views.user_info, name="user_info"),
    path('', include('dj_rest_auth.urls')),
    # path('signup/', CustomRegisterView.as_view(), name="rest_register"),
    path('delete/', views.user_delete, name='user_delete'),
    path('changepassword/', change_password),
    path('find/', views.find_password),
]