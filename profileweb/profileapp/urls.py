from django.contrib import admin
from django.urls import path

from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import view_profile, edit_profile
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('', views.index,name="homepage"),
    path('', views.login_view, name="login  page"),
    path('forgot', views.forgot,name="homepage"),
    path('otprequest', views.otprequest, name="homepage"),
    path('create_account', views.registration_view, name="homepage"),
    path('accounts/profile/', view_profile, name='view_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/login/', LoginView.as_view(template_name='index.html'), name='login'),
    path('apiview/',views.api_account, name='api'),

]
