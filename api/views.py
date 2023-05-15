from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets

from tienda.models import Categoria, Producto
from .serializers import(
    CategoriaSerializer,
    ProductoSerializer
)

class CategoriaView(APIView):
    def get(self, request):
        lista_categorias = Categoria.objects.all()
        serializer_categoria = CategoriaSerializer(lista_categorias, many=True)
        return Response(serializer_categoria.data)

class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    lookup_url_kwarg = 'categoria_id'
    serializer_class = CategoriaSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductoView(APIView):
    def get(self, request):
        lista_producto = Producto.objects.all()
        serializer_producto = ProductoSerializer(lista_producto, many=True)
        return Response(serializer_producto.data)