from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView

from .models import *


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



class MahsulotTahrirlashView(View):
    def get(self, request, pk):
        mahsulot = get_object_or_404(Mahsulot, pk=pk)
        context = {'product': mahsulot}
        return render(request, 'mahsulot-tahrirlash.html', context)

    def post(self, request, pk):
        mahsulot = get_object_or_404(Mahsulot, pk=pk)
        mahsulot.nom = request.POST.get('name')
        mahsulot.brand = request.POST.get('brand_name')
        mahsulot.narx1 = request.POST.get('price')
        mahsulot.miqdor = request.POST.get('amount')
        mahsulot.save()
        return redirect('mahsulot_tahrirlash', pk=pk)

class MahsulotOchirishView(View):
    def post(self, request, mahsulot_id):
        mahsulot = get_object_or_404(Mahsulot, pk=mahsulot_id)
        mahsulot.delete()
        return redirect('mahsulotlar')


class MijozlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            mijozlar = Mijoz.objects.filter(tarqatuvchi=request.user)
            return render(request, 'mijozlar.html', {'mijozlar': mijozlar})
        return redirect('login')