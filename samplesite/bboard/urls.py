from django.urls import path

from .views import index, by_rubric

urlpatterns = [
    path('<int:rubrick_id>/',by_rubric, name='by_rubic'),
    path('', index, name='index'),
] 