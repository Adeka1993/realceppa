from django.urls import path
from .views import SignUpView, ProfileUpdate, EmailUpdate, MiPerfil

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('profile/', ProfileUpdate.as_view(), name="profile"),
    path('mi-perfil/', MiPerfil.as_view(), name="my-profile"),
    path('profile/email/', EmailUpdate.as_view(), name="profile_email")


]