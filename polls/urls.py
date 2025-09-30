from django.urls import path
from polls import views

urlpatterns = [
    path('', views.index, name='index'),
    path('run_thread', views.run_thread),

    # Question endpoints
    path('api/questions/', views.QuestionListCreateView.as_view(), name='question-list'),
    path('api/questions/<int:pk>/', views.QuestionDetailView.as_view(), name='question-detail'),

    # Choice endpoints
    path('api/choices/', views.ChoiceListCreateView.as_view(), name='choice-list'),
    path('api/choices/<int:pk>/', views.ChoiceDetailView.as_view(), name='choice-detail'),

    # FlightLeg endpoints
    path('api/flight-legs/', views.FlightLegListCreateView.as_view(), name='flightleg-list'),
    path('api/flight-legs/<int:pk>/', views.FlightLegDetailView.as_view(), name='flightleg-detail'),

    # Flight endpoints
    path('api/flights/', views.FlightListCreateView.as_view(), name='flight-list'),
    path('api/flights/<int:pk>/', views.FlightDetailView.as_view(), name='flight-detail'),

    # Publication endpoints
    path('api/publications/', views.PublicationListCreateView.as_view(), name='publication-list'),
    path('api/publications/<int:pk>/', views.PublicationDetailView.as_view(), name='publication-detail'),

    # Article endpoints
    path('api/articles/', views.ArticleListCreateView.as_view(), name='article-list'),
    path('api/articles/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
]