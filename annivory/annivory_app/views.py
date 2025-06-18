from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render, redirect

from .forms import SignupForm

from rest_framework.views import APIView
from rest_framework.response import Response


'''
회원가입 및 로그인 처리
홈 페이지로 리디렉션
'''

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'message': 'CSRF token set'})


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'auth/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')



# /hello/ 주소 참고
def hello(request):
    return HttpResponse("Hello, world. You're at the polls page.")

class SampleAPI(APIView):
    def get(self, request):
        data = {'message': 'Hello from Django API!'}
        return Response(data)

class ReactAppView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['STATIC_URL'] = settings.STATIC_URL
        return context

serve_react = ReactAppView.as_view()