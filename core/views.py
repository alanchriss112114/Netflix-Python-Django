from django.views import View
from django.shortcuts import render

# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')