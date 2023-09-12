from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world! You're at the polls index.")


def run_thread(request):
    return HttpResponse("Task successfully started!")