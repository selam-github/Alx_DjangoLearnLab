from django.urls import path
from .views import example_view

urlpatterns = [
    path('example-form/', example_view, name='example_view'),
    # Other URL patterns
]