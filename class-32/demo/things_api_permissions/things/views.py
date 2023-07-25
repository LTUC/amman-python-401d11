from django.shortcuts import render
from .models import Thing,Post
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import ThingSerializer,PostSerializer

from rest_framework.permissions import AllowAny
from .permissions import IsOwnerOrReadOnly
# Create your views here.

# class ThingListView(ListAPIView):
class ThingListView(ListCreateAPIView):

    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    permission_classes = [IsOwnerOrReadOnly]


class PostListView(ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]


class  PostDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
