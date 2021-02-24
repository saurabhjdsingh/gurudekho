from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('confirm_your_account', views.confirm_your_account, name="confirm_your_account"),
    path('account_activated', views.account_activated, name="account_activated"),
    path('account_activated_false', views.account_activated_false, name="account_activated_false"),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]