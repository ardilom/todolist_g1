from .models import Tarea
from rest_framework import viewsets
from .serializers import TareaSerializer


class TareaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tarea.objects.all().order_by('id')
    serializer_class = TareaSerializer