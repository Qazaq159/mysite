from django.http.response import HttpResponse
from django.http import JsonResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world! You're at the polls index.")


def run_thread(request):
    import time
    time.sleep(5)
    return JsonResponse({"body": "Task successfully started!"})
