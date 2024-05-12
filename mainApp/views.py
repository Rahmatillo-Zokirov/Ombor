from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView

from .models import *
from statsApp.models import *

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')



class BolimView(View):
    def get(self, request):
        return render(request, 'bolimlar.html')




class MahsulotlarView(View):

    def get(self, request):
        if request.user.is_authenticated:
            mahsulotlar = Mahsulot.objects.filter(tarqatuvchi=request.user)
            content = {
                'mahsulotlar': mahsulotlar
            }
            return render(request, 'mahsulotlar.html', content)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            Mahsulot.objects.create(
                tarqatuvchi=request.user,
                nom = request.POST.get('nom'),
                brand = request.POST.get('brand'),
                narx1 = request.POST.get('narx1'),
                narx2 = request.POST.get('narx2'),
                miqdor = request.POST.get('miqdor'),
                olchov = request.POST.get('olchov'),
                sana = request.POST.get('sana'),
            )
            return redirect('mahsulotlar')
        return redirect('login')



class MahsulotTahrirlashView(View):
    def get(self, request, pk):
        mahsulot = get_object_or_404(Mahsulot, pk=pk)
        context = {'product': mahsulot}
        return render(request, 'mahsulot-tahrirlash.html', context)

    def post(self, request, pk):
        if request.user.is_authenticated:
            mahsulot = get_object_or_404(Mahsulot, pk=pk)
            mahsulot.nom = request.POST.get('name')
            mahsulot.brand = request.POST.get('brand_name')
            mahsulot.narx1 = request.POST.get('price')
            mahsulot.miqdor = request.POST.get('amount')
            mahsulot.save()
            return redirect('mahsulotlar',)
        return redirect('login')


class MijozlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            mijozlar = Mijoz.objects.filter(tarqatuvchi=request.user)
            return render(request, 'mijozlar.html', {'mijozlar': mijozlar})
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            Mijoz.objects.create(
                tarqatuvchi=request.user,
                ism = request.POST.get('ism'),
                dokon = request.POST.get('dokon'),
                tel = request.POST.get('tel'),
                manzil = request.POST.get('manzil'),
                qarz = request.POST.get('qarz'),
            )
            return redirect('mijozlar')
        return redirect('login')


class MahsulotDeleteView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mahsulot = Mahsulot.objects.get(pk=pk)
            if mahsulot.tarqatuvchi == request.user:
                mahsulot.delete()
            return redirect('mahsulotlar')
        return redirect('login')


class MahsulotQidirishView(View):
    def get(self, request):
        nom_query = request.GET.get('q_nom')
        brand_query = request.GET.get('q_brand')

        mahsulotlar = Mahsulot.objects.filter(nom__icontains=nom_query, brand__icontains=brand_query)

        context = {
            'mahsulotlar': mahsulotlar,
        }
        return render(request, 'mahsulotlar.html', context)

class MijozlarDelete(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mijoz = Mijoz.objects.get(pk=pk)
            if mijoz.tarqatuvchi == request.user:
                mijoz.delete()
            return redirect('mahsumijozlarlotlar')
        return redirect('login')


class MijozTahrirlashView(View):
    def get(self, request, pk):
        mijoz = get_object_or_404(Mijoz, pk=pk)
        context = {'product': mijoz}
        return render(request, 'mijoz-tahrirlash.html', context)

    def post(self, request, pk):
        if request.user.is_authenticated:
            mijoz = get_object_or_404(Mijoz, pk=pk)
            mijoz.ism = request.POST.get('ism')
            mijoz.dokon = request.POST.get('dokon')
            mijoz.tel = request.POST.get('tel')
            mijoz.manzil = request.POST.get('manzil')
            mijoz.qarz = request.POST.get('qarz')
            mijoz.save()
            return redirect('mijozlar',)
        return redirect('login')



class MijozDeletView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mijoz = Mijoz.objects.get(pk=pk)
            if mijoz.tarqatuvchi == request.user:
                mijoz.delete()
            return redirect('mijozlar')
        return redirect('login')
