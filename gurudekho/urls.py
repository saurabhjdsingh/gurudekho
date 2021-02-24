from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,  name='index'),
    path('', include("accounts.urls", namespace="accounts")),
    path('', include("dashboard.urls", namespace="dashboard")),
    path('accounts/', include('allauth.urls')),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)