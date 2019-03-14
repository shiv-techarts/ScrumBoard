from rest_framework.viewsets import ModelViewSet
from .models import List, Card
from .serializers import ListSerializer, CardSerializer


class ListApiSet(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class CardApiSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
