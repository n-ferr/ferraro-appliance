from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(['POST'])
@permission_classes([AllowAny])
def Tests(request):
    current_value = int(request.data.get('value'))
    new_value = current_value + 1
    print(new_value)
    return Response({
        'value': new_value
    })

