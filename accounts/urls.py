from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('users/profile/', views.getUserProfile, name='user-profile'),
    path('api/v1/', include('djoser.urls'), name='djoser'),
    path('jwt/create/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]