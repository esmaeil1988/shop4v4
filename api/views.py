from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from app1.models import product
from .serializers import productSerializer

# Create your views here.
class vproduct(APIView):
    authentication_classes = (TokenAuthentication,)
    def get(self,request):
        q=product.objects.all()
        ser=productSerializer(q,many=True)
        return Response(ser.data)
    
    def post(self,request):
        if request.user.is_authenticated:
            ser=productSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                return Response({"message":"Successed"})
            return Response(ser.errors)
        else:
            return Response({"message":"invalid user"})
    
    def put(self,request):
        i=product.objects.get(id=request.data['id'])
        ser=productSerializer(data=request.data,instance=i,partial=True)
        if ser.is_valid():
            ser.save()
            return Response({"message":"Successed"},status=201)
        return Response(ser.errors)
    
    def delete(self,request):
        i=product.objects.get(id=request.data['id'])
        i.delete()
        return Response({"message":"Successed"},status=201)
