from django.urls import path
from .views import ListCreateViews,UpdateDeleteViews

urlpatterns = [
    path('', ListCreateViews.as_view()),
    path('update/<int:pk>/',UpdateDeleteViews.as_view()),

]
