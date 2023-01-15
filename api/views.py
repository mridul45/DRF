from django.shortcuts import render
from .models import *
from django.http import HttpResponse,JsonResponse
from .serializers import *
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User


class ArticleViewSet(viewsets.ModelViewSet):
    
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	permission_classes = [IsAuthenticated]
	authentication_classes = (TokenAuthentication,)


class UserViewSet(viewsets.ModelViewSet):

	queryset = User.objects.all()
	serializer_class = UserSerializer