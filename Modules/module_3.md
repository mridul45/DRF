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


# ListModelMixin --> To Get the views or data from models
# CreateModelMixin --> To POST the data from Mixin
# RetriveModelMixin --> To retrieve a particular data
# UpdateModelMixin --> To update the model from backend
# DestroyModelMixin --> To delete the data.


# APIView is a base class. It doesn't assume much and will allow you to plug pretty much anything to it.

# GenericAPIView is meant to work with Django's Models. It doesn't assume much beyond all the bells and whistles the 	Model introspection can provide.



class ArticleList(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

	def get(self,request):
		return self.list(request)
	
	def post(self,request):
		return self.create(request)
	

class ArticleDetail(
		generics.GenericAPIView,
		mixins.RetrieveModelMixin,
		mixins.UpdateModelMixin,
		mixins.DestroyModelMixin):
	
	lookup_field = 'id'
	
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

	def get(self,request,id):
		return self.retrieve(request,id=id)
	
	def put(self,request,id):
		return self.update(request,id=id)
	
	def delete(self,request,id):
		return self.destroy(request,id=id)