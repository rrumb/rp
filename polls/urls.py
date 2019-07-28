from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('<int:elevator>/', views.elevator_check, name='elevator_check'),

    path('<int:elevator>/<int:status>/', views.status_update, name='status_update')
]
