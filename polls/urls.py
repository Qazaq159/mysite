from django.conf.urls import url
from polls import views

urlpatterns = [
    url('', views.index, name='index'),
    url('run_thread', views.run_thread)
]