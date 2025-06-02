from django.conf import settings
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

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