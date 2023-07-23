from django.shortcuts import render
from .models import Thing
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import ThingSerializer
# Create your views here.

# class ThingListView(ListAPIView):
class ThingListView(ListCreateAPIView):

    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


