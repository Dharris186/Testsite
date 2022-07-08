from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    page = "<html><head><title>Test Page</title></head><body><h1>Finally Something I know</h1></body></html>"
    return HttpResponse(page)
