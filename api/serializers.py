from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		
		model = Article
		fields = "__all__"

	# def create(self,validated_data):
	# 	return Article.objects.create(validated_data)

	# def update(self,instance,validated_data):
	# 	instance.title = validated_data.get('title',instance.title)
	# 	instance.description = validated_data.get('description',instance.description)

class UserSerializer(serializers.ModelSerializer):
	class Meta:

		model = User
		fields = ['id','username','password']

		extra_kwargs = {'password': {
			'write_only':True,
			'required': True
		}}

	def create(self,validated_data):
		user = User.objects.create_user(**validated_data)
		Token.objects.create(user=user)
		return user