from django.urls import path
from . import views

urlpatterns = [
    path('', views.track_list, name='track_list'),
    path('<int:track_id>/students/', views.show_students, name='show_students'),
]
