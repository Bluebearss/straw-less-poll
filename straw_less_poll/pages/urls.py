from django.urls import path
from . import views

# Page url where any '/' points to this loader page. By default it goes to /
urlpatterns = [
    path('', views.index, name='index'),
]
