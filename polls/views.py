import time
from django.http.response import HttpResponse
from django.http import JsonResponse
from rest_framework import generics

from polls.models import (
    Question,
    QuestionData,
    Choice,
    FlightLeg,
    Flight,
    Publication,
    Article,
)
from polls.serializers import (
    QuestionSerializer,
    QuestionDataSerializer,
    ChoiceSerializer,
    FlightLegSerializer,
    FlightSerializer,
    PublicationSerializer,
    ArticleSerializer,
)


def index(request):
    return HttpResponse("Hello, world! You're at the polls index.")


def run_thread(request):
    import time
    time.sleep(6)
    return JsonResponse({"body": "Task successfully started"})


# Question
class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all().order_by('-id')
    serializer_class = QuestionSerializer


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all().order_by('-id')
    serializer_class = QuestionSerializer


# Choice
class ChoiceListCreateView(generics.ListCreateAPIView):
    queryset = Choice.objects.all().order_by('-id')
    serializer_class = ChoiceSerializer


class ChoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all().order_by('-id')
    serializer_class = ChoiceSerializer


# FlightLeg
class FlightLegListCreateView(generics.ListCreateAPIView):
    queryset = FlightLeg.objects.all().order_by('-id')
    serializer_class = FlightLegSerializer


class FlightLegDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FlightLeg.objects.all().order_by('-id')
    serializer_class = FlightLegSerializer


# Flight
class FlightListCreateView(generics.ListCreateAPIView):
    queryset = Flight.objects.all().order_by('-id')
    serializer_class = FlightSerializer


class FlightDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all().order_by('-id')
    serializer_class = FlightSerializer


# Publication
class PublicationListCreateView(generics.ListCreateAPIView):
    queryset = Publication.objects.all().order_by('-id')
    serializer_class = PublicationSerializer


class PublicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publication.objects.all().order_by('-id')
    serializer_class = PublicationSerializer


# Article
class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all().order_by('-id')
    serializer_class = ArticleSerializer


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all().order_by('-id')
    serializer_class = ArticleSerializer
