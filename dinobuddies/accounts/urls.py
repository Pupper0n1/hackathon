from django.urls import include, path
from django.contrib.auth import views as authenticator_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', authenticator_views.LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', authenticator_views.LogoutView.as_view(), name="logout"),
    path('signup', views.SignUp.as_view(), name='signup')
]