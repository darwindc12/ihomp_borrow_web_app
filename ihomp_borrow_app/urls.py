from django.urls import path
from . import views

urlpatterns = [
    path('', views.CombinedListView.as_view(), name='home'),
]