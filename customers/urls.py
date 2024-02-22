from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    # Define other URL patterns for CRUD operations
]
