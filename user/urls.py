from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.views import CreateUserView, LoginUserView, ManageUserView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='create'),
    path('login/', LoginUserView.as_view(), name='get_token'),
    path('me/', ManageUserView.as_view(), name='manage_user'),
    path("login/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

app_name = 'user'
