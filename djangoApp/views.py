import json
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework.response import Response

# Create your views here.



@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([AllowAny])
def home(request):
    return JsonResponse({"status":"CI/CD ssuccess"}, status=status.HTTP_201_CREATED) 
    # return Response({"status":"success"}, status=status.HTTP_201_CREATED)

    # if request.method == 'GET':
    #     return JsonResponse({"status":"success"}, status=status.HTTP_201_CREATED) 
        # return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        # return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)