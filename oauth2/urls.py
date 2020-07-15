from django.urls import path, include
from .views import AuthenticationView, LogoutView

urlpatterns = [
    path('openid/', include('oidc_provider.urls', namespace='oidc_provider')),
    path('authenticate', AuthenticationView.as_view(), name="authenticate"),
    path('logout', LogoutView.as_view(), name="logout"),
]
