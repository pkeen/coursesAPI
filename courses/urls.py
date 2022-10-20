from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:course_slug>/', views.course_detail, name='course_detail'),
    path('<str:course_slug>/<str:lesson_slug>', views.lesson_detail, name='lesson_detail')
]