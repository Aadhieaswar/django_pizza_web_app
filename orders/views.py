from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
    'msg': "Hello!"
    }
    return render(request, "orders/index.html", context)