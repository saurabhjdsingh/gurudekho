from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "dashboard"

urlpatterns = [
    path('aftersignup', views.aftersignup, name='aftersignup'),
    path('editprofile', views.editprofile, name='editprofile'),
    path('profile', views.profile, name='profile'),
    path('tutors', views.tutors, name='tutors'),
    path('tutor/<str:username>', views.detail, name='detail'),
    path('pro_member', views.pro_member, name='pro_member'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)