from django.urls import path
from . import views

urlpatterns = [
    path('', views.CombinedListView.as_view(), name='home'),
    path('borrow/', views.borrow_form, name='borrow'),
    path('get_peripherals/<int:category_id>/', views.get_peripherals, name='get_peripherals'),
    path('get_unique_number/<int:peripheral_id>/', views.get_unique_number, name='get_unique_number'),


]