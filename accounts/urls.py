from django.urls import path, include, re_path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('users/profile/', views.getUserProfile, name='user-profile'),
    #re_path('accounts/users/activate/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', views.UserActivationView.as_view()),
    path('accounts/', include('djoser.urls'), name='djoser'),
    
    path('jwt/create/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]