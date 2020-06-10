from django.urls import path
from . import views

# New polls app urls where any '/polls/...' points to this app page. By default it goes to polls/index.html
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]
