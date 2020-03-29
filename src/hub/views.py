from django.http import JsonResponse
from django.shortcuts import render

# third party imports
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

"""from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView"""

from .serializer import PostSerializer
from .models import Post


class PostView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    # def perform_create(self, serializer):
    #     # Send mail
    #     serializer.save()
#
# class TestView(APIView):
#     permission_classes = [IsAuthenticated, ]
#
#     def get(self, *args, **kwargs):
#         qs = Post.objects.all()
#         post = qs.first()
#         # serializer = PostSerializer(qs, many=True)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
