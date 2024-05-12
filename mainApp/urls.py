from django.urls import path
from .views import *
from statsApp.views import *


urlpatterns = [
    path('bolimlar/', BolimView.as_view(), name='bolimlar'),
    path('mahsulotlar/', MahsulotlarView.as_view(), name='mahsulotlar'),
    path('mahsulotlar/<int:pk>/tahrirlash/', MahsulotTahrirlashView.as_view(), name='mahsulot_tahrirlash'),
    path('mahsulotlar/<int:pk>/ochirish/', MahsulotDeleteView.as_view(), name='mahsulot_ochirish'),
    path('mijozlar/', MijozlarView.as_view(), name='mijozlar'),
    path('mahsulotlar/', MahsulotQidirishView.as_view(), name='mahsulot_qidirish'),
    path('mijozlar/<int:pk>/tahrirlash/', MijozTahrirlashView.as_view(), name='mijozlar_tahrirlash'),
    path('statistikalar/', StatistikalarView.as_view(), name='statistikalar'),
    path('mijozlar/<int:pk>/ochirish/', MijozDeletView.as_view(), name='mijozlar_ochirish'),
]
