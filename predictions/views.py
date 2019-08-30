from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
import predictions.predict_image as pi
from rest_framework.response import Response
# from rest_framework.auth.model import model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

# Create your views here.
class Prediction():
    pass

class P():
    pass

def makePrediction():
    pass
    
@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    username = 'ratnesh'
    password = 'emorphis'
    if username is None or password is None:
        return Response({'result': 'Please provide proper credentials'}, status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'result': 'Invalid credentials'}, status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token':token.key}, status=HTTP_200_OK)

@csrf_exempt
@api_view(['GET'])
def sample(request):
    data = {'sample_data': 123,'d': 123}
    return Response(data, status=HTTP_200_OK) 

@csrf_exempt
@api_view(['POST'])
def image_prediction(request):
    img = request.POST['img']
    imgfile = pi.parse(img)
    return Response(imgfile, status=HTTP_200_OK)