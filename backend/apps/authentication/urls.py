from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import ObtainTokenPairView

urlpatterns = [
    path('token/', ObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]