from django.urls import path
from . import views

urlpatterns = [
    path('resume/', views.index, name="resume_index"),
    #path('resume/test', views.test, name="resume_test"),
]