from django.urls import path
from .views import add_order, search_order
urlpatterns = [
    path('add_order/', add_order, name='add_order'),
    path('', search_order, name='search_order'),
]