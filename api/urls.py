from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles',ArticleViewSet,basename='articles')
router.register('users',UserViewSet,basename='users')

urlpatterns = [
	# path('',ArticleList.as_view()),
    # path('article/<int:id>/',ArticleDetail.as_view()),
	path('',include(router.urls)),
]
