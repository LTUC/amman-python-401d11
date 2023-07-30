from django.urls import path

from .views import ThinglistView,ThingDetailView
urlpatterns = [
   
   path('',ThinglistView.as_view(), name= 'thing_list'),
   path('<int:pk>/',ThingDetailView.as_view(), name= 'thing_detail')

]
