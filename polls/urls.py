from django.urls import path
from polls import views

urlpatterns = [
    path('', views.index, name='index'),
    path('run_thread', views.run_thread)
]