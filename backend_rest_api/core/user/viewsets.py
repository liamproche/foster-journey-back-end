from core.user.serializers import UserSerializer
from core.user.models import User
from rest_framework import viewsets 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django.shortcuts import get_object_or_404


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    
    
    # def list(self, request):
    #     return Response(serializer_class.data)
    # def retrieve (self, request, pk=None):
    #     user = get_object_or_404(self.queryset, pk=pk)
    #     serializer_class = UserSerializer(user)
    #     return Response(serializer_class.data)
    
    # http_method_names = ['get']

    
    
    
    
    
    
    
    
    

    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['created']
    # ordering = ['-created']

    
    
    
    
    
    
    
    # def get_queryset(self):
    #     # if self.request.user.is_superuser:
    #         return User.objects.all()

    # def get_object(self):
    #     lookup_field_value = self.kwargs[self.lookup_field]
    #     obj = User.objects.get(lookup_field_value)
    #     self.check_object_permissions(self.request, obj)
    #     return obj
