from django.urls import path
from .views import registration
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('register/', registration, name='register'), #DONE
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"), #DONE
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('hello/', views.HelloView.as_view(), name='hello'), #DONE
    path('home/', views.home, name='home'), #DONE
]