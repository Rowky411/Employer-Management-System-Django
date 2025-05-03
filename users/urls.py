from django.urls import path
from .views import EmployerDetailUsingIdView, EmployerListView, RegisterView, UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('auth/signup/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/profile/', UserProfileView.as_view(), name='user_profile'),
    path('employers/', EmployerListView.as_view(), name='employer_list'),
    path('employers/<int:pk>/', EmployerDetailUsingIdView.as_view(), name='employer_detail'),
]