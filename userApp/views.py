from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('bolimlar')  # Foydalanuvchi autentifikatsiya qilganda qayerga o'tishini aniqlang
        else:
            return redirect('login')  # Autentifikatsiya qilinmagan holatda login sahifasiga qaytish

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')  # Chiqish so'ngida login sahifasiga qaytish



