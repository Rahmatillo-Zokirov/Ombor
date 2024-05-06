from django.shortcuts import render
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

class MijozlarView(View):
    def get(self, request):
        return render(request, 'mijozlar.html')



class BolimView(View):
    def get(self, request):
        return render(request, 'bolimlar.html')


class MahsulotlarView(View):
    def ge(self, request):
        return render(request, 'mahsulotlar.html')
