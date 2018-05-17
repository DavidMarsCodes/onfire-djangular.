
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login as login_auth,
    logout as logout_auth,

    )

    
User = get_user_model()

#####
#SERIALIZERS imports
#####
from .serializers import (
    UsuarioSerializer, 
    UsuarioCrearActualizarSerializer, 
    UsuarioListarSerializer, 
    UsuarioDetalleSerializer
)

######
#VIEWS imports
######
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)
#
#PERMISOS
#
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

# class UserAPIViewset(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UsuarioSerializer
    


class CurrentUserView(APIView):
    def get(self, request):
        serializer = UsuarioDetalleSerializer(request.user)
        return Response(serializer.data)


class UsuarioCrearAPIView(CreateAPIView):
    """
    Serializador para crear un usuario
    """
    serializer_class = UsuarioCrearActualizarSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

class UsuarioListarAPIView(ListAPIView):
    """
    Serializador para LISTAR TODOS LOS USUARIOS
    """
    queryset = User.objects.all()
    serializer_class = UsuarioListarSerializer
    permission_classes = [IsAuthenticated]

class UsuarioDetalleByIdAPIView(RetrieveAPIView):
    """
    Serializador para ver detalles de un USUARIO por ID
    """
    queryset = User.objects.all()
    serializer_class = UsuarioDetalleSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class UsuarioEditarAPIView(RetrieveUpdateAPIView):
    """
    Serializador para editar un USUARIO por ID
    """
    queryset = User.objects.all()
    serializer_class = UsuarioCrearActualizarSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        

class UsuarioEliminarAPIView(DestroyAPIView):
    """
    Serializador par eliminar un usuario por ID
    """
    queryset = User.objects.all()
    serializer_class = UsuarioDetalleSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]



