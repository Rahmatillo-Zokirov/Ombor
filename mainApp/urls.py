from django.urls import path
from .views import *

urlpatterns = [
    path('bolimlar/', BolimView.as_view(), name='bolimlar'),
    path('mahsulotlar/', MahsulotlarView.as_view(), name='mahsulotlar'),
    path('mijozlar/', MijozlarView.as_view(), name='mijozlar'),
    path('mahsulotlar/<int:pk>/tahrirlash/', MahsulotTahrirlashView.as_view(), name='mahsulot_tahrirlash'),
    path('mahsulotlar/<int:pk>/ochirish/', MahsulotDeleteView.as_view(), name='mahsulot_ochirish'),
    path('mijozlar/', MijozlarView.as_view(), name='mijozlar')
]
