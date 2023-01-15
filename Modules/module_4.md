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


# Using ViewSet

# In urls.py --->
# from django.contrib import admin
# from django.urls import path,include
# from .views import *
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('articles',ArticleViewSet,basename='articles')

# urlpatterns = [
# 	  path('',ArticleList.as_view()),
#     path('article/<int:id>/',ArticleDetail.as_view()),
# 	path('',include(router.urls)),
# ]


class ArticleViewSet(viewsets.ViewSet):
    
	def list(self,request):
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles,many=True)
		return Response(serializer.data)

	
	def create(self,request):

		serializer = ArticleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)

		return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
	

	def retrieve(self,request,pk=None):

		queryset = Article.objects.all()
		article = get_object_or_404(queryset,pk=pk)
		serializer = ArticleSerializer(article)

		return Response(serializer.data)
	
	def update(self,request,pk=None):

		article = Article.objects.get(pk=pk)
		serializer = ArticleSerializer(article,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)

		return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


	def destroy(self,request,pk=None):

		article = Article.objects.get(pk=pk)
		article.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)