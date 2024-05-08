from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from statsApp.views import *
from mainApp.views import *
from userApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('mainApp.urls')),
    path('user/', include('userApp.urls')),
    path('', LoginView.as_view(), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

