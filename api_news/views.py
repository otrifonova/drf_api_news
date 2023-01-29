from rest_framework.viewsets import ModelViewSet
from .models import Type, News
from .serializers import TypeSerializer, NewsSerializer


class APITypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class APINewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_queryset(self):
        queryset = News.objects.all()
        type = self.request.query_params.get('type_id')
        if type:
            queryset = News.objects.filter(type=type)
        return queryset
