from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from mainApp.models import Mahsulot, Mijoz
from statsApp.models import *


class StatistikalarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            sotuvlar = Sotuv.objects.filter(tarqatuvchi=request.user)
            mahsulotlar = Mahsulot.objects.filter(tarqatuvchi=request.user)
            mijozlar = Mijoz.objects.filter(tarqatuvchi=request.user)
            summa = sum(sotuvlar.values_list('summa', flat=True))
            qarz = sum(sotuvlar.values_list('qarz', flat=True))
            context = {
                'sotuvlar': sotuvlar,
                'mahsulotlar': mahsulotlar,
                'mijozlar': mijozlar,
                'summa': summa,
                'qarz': qarz
            }
            return render(request, 'statistikalar.html', context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            summa = request.POST.get('summa', None)
            mahsulot = Mahsulot.objects.get(id=request.POST.get('mahsulot'))
            miqdor = float(request.POST.get('miqdor'))
            mijoz = Mijoz.objects.get(id=request.POST.get('mijoz'))
            if int(summa) == 0:
                summa = float(mahsulot.narx2) * miqdor
            tolandi = float(request.POST.get('tolandi'))
            qarz = float(request.POST.get('qarz'))
            if tolandi == 0 and qarz == 0:
                qarz = summa
            elif tolandi == 0 and qarz != 0:
                if summa < qarz:
                    return redirect('statistikalar')
                tolandi = summa - qarz
            elif tolandi != 0 and qarz == 0:
                if summa < tolandi:
                    return redirect('statistikalar')
                qarz = summa - tolandi
            sana = request.POST.get('sana')
            if sana == '2000-01-01':
                sana = datetime.now().strftime('%Y-%m-%d')
            if float(miqdor) > float(mahsulot.miqdor):
                return redirect('statistikalar')
            Sotuv.objects.create(
                tarqatuvchi=request.user,
                mahsulot=mahsulot,
                mijoz=mijoz,
                miqdor=miqdor,
                summa=summa,
                tolandi=tolandi,
                qarz=qarz,
                sana=sana
            )
            mahsulot.miqdor -= miqdor
            mahsulot.save()
            mijoz.qarz = sum(Sotuv.objects.filter(tarqatuvchi=request.user, mijoz=mijoz).values_list('qarz', flat=True))
            mijoz.save()
            return redirect('statistikalar')
        return redirect('login')


class StatikDeletView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            sotuv = Sotuv.objects.get(id=pk)
            if sotuv.tarqatuvchi == request.user:
                sotuv.delete()
            return redirect('statistikalar')
        return redirect('login')


class StatikUpdateView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            sotuv = Sotuv.objects.get(tarqatuvchi=request.user, id=pk)
            mahsulot = Mahsulot.objects.get(pk=sotuv.mahsulot.id, tarqatuvchi=request.user)
            mijoz = Mijoz.objects.get(id=sotuv.mijoz.pk, tarqatuvchi=request.user)
            context = {
                'sotuv': sotuv,
                'mahsulot': mahsulot,
                'mijoz': mijoz,
            }
            return render(request, 'statistika-tahrirlash.html', context)
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:
            sotuv = Sotuv.objects.get(tarqatuvchi=request.user, id=pk)
            miqdor = float(request.POST.get('miqdor'))
            mahsulot = sotuv.first().mahsulot

            if mahsulot.miqdor >= (miqdor[0] - float(sotuv.first().miqdor())):
                mahsulot.miqdor + float(sotuv.first().miqdor) - miqdor[0]
                mahsulot.save()

            qarz = request.POST.get('qarz')
            tolandi = request.POST.get('tolandi')
            summa = request.POST.get('summa')
            if sotuv.first().miqdor != miqdor[0]:
                summa = float(sotuv.first().mahsulot.nax2) * miqdor[0]
            qarz = float(summa) - float(tolandi)
            sotuv.update(
                tarqatuvchi=request.user,
                mahsulot=mahsulot,
                miqdor=miqdor,
                summa=summa,
                qarz=qarz

            )