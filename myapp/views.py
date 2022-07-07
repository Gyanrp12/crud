from django.shortcuts import render
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer 
from rest_framework import status
from rest_framework .views import APIView
 
class UserAPI(APIView):
    def get(self, request,pk=None,format=None):
        id=pk
        if id is not None:
            usr = User.objects.get(id=id)
            ser = UserSerializer(usr)
            return Response(ser.data)
        usr = User.objects.all()
        ser = UserSerializer(usr, many=True)
        return Response(ser.data)
    def post(self, request,format=None):
        ser = UserSerializer(data=request.data)
        if ser.is_valid(): 
            ser.save()
            return Response({'msg':'data Created'},status =status.HTTP_201_CREATED)
        return Response(ser.errors)
    def patch(self, request, pk, format=None):
                                                                                                                                                                                                                          
        id=pk
        usr = User.objects.get(id=id)
        ser = UserSerializer(usr, data=request.data, partial=True)
        if ser.is_valid():
            
            ser.save()
            return Response({'msg':" patch data is updated"})
        return Response(ser.errors)
    def put(self, request,pk,format=None):
        id=pk
        usr = User.objects.get(id=id)
        ser = UserSerializer(usr,data=request.data )
        if ser.is_valid():
            ser.save()
            return Response({'msg':"put data is updated"})
        return Response(ser.errors)
        
    def delete(self,request,pk,format=None):
        id=pk
        usr = User.objects.get(id=id)
        usr.delete()
        return Response({'msg':"deleted"})