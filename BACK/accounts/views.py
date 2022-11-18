from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def account_detail(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)