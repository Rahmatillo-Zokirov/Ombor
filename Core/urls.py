from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from statsApp.views import *
from mainApp.views import *
from userApp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('statistika/', StatistikaView.as_view(), name='statistika'),
    path('mijozlar/', MijozlarView.as_view(), name='mijozlar'),
    path('', LoginView.as_view(), name='login'),
    path('bolimlar/', BolimView.as_view(), name='bolimlar'),
    path('mahsulotlar/', MahsulotlarView.as_view(), name='mahsulotlar')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
