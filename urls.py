from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('destroy/<int:course_id>', views.show),
    path('destroy/<int:course_id>/destroycomplete', views.destroy),
]
