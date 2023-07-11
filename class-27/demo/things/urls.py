from django.urls import path
from .views import HomeView,ThingsListView,ThingDetailsView

urlpatterns = [
 
    path('',HomeView.as_view(), name='home'),
    path('things/',ThingsListView.as_view(), name='things'),
    path('things/<pk>/',ThingDetailsView.as_view(), name='thing_details')
]
