from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/<int:show_id>', views.profile),
    path('shows/<int:show_id>/edit', views.edit),
    path('shows/<int:show_id>/update', views.update),
    path('shows/new', views.new),
    path('shows/create', views.add_show),
    path('shows/<int:show_id>/destroy', views.destroy),
]