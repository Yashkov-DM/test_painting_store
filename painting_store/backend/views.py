from rest_framework import generics
from .models import Store
from .serializers import StoreSerializer


class StoreView(generics.ListAPIView,
                generics.RetrieveAPIView,
                generics.CreateAPIView,
                generics.UpdateAPIView,
                generics.DestroyAPIView,
                generics.GenericAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def get(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

