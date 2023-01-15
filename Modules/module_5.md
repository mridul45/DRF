# <-------------- Generic ViewSets ----------------->

class ArticleViewSet(
		viewsets.GenericViewSet,
		mixins.ListModelMixin,
		mixins.CreateModelMixin,
		mixins.RetrieveModelMixin,
		mixins.UpdateModelMixin,
		mixins.DestroyModelMixin
		):
    
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer