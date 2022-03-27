from django.shortcuts import render

from rest_framework.decorators import api_view
import io
from rest_framework.parsers import JSONParser
from .serializer import buildingSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from .serializer import ownerSerializer
from .serializer import roomSerializer
from .serializer import customeraccountSerializer
from .serializer import allbillsSerializer
@api_view(['POST'])

def addbuilding(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = buildingSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.validated_data
            serializer.create(serializer.validated_data)
            res = {'msg','building create successfully'}
            return Response({"msg", "oaky"},status=status.HTTP_200_OK)
        else:
            return Response({"msg":"Eror"},status=status.HTTP_400_BAD_REQUEST)
 #####################OWNER#######################
@api_view(['POST'])
def addowner(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = ownerSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.validated_data
            res = {'msg', 'building create successfully'}
            return Response({"msg", "oaky"}, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "Eror"}, status=status.HTTP_400_BAD_REQUEST)
###########ADD Rooms
@api_view(['POST'])
def addroom(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = roomSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.validated_data
            res = {'msg', 'building create successfully'}
            return Response({"msg", "oaky"}, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "Eror"}, status=status.HTTP_400_BAD_REQUEST)
############Customer Account
@api_view(['POST'])
def addcustomer(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = customeraccountSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.validated_data
            res = {'msg', 'building create successfully'}
            return Response({"msg", "oaky"}, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "Eror"}, status=status.HTTP_400_BAD_REQUEST)

################ bills
@api_view(['POST'])
def customerbills(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = allbillsSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.validated_data
            res = {'msg', 'building create successfully'}
            return Response({"msg", "oaky"}, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "Eror"}, status=status.HTTP_400_BAD_REQUEST)


