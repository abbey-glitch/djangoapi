# from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework.response import Response
# from rest_framework.exceptions import NotFound
# from rest_framework.decorators import api_view
# from rest_framework.parsers import JSONParser
# from rest_framework import status
# from rest_framework import serializers
# from .models import Users
# from .serializers import UsersSerializer
# # Create your views here.
# class UsersProfile:

#         # 1. List all
#     def get(self, request, *args, **kwargs):
#       '''
#       List all the todo items for given requested user
#       '''
#       todos = Users.objects.filter(user = request.user.id)
#       serializer = UsersSerializer(todos, many=True)
#       return Response(serializer.data, status=status.HTTP_200_OK)
    

#         # 2. Create
#     def post(self, request, *args, **kwargs):
#       '''
#       Create a new user item
#       '''
#       serializer = UsersSerializer(data=request.data)
#       if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # test endpoints
# @api_view(['GET', 'POST', 'DELETE'])
# def userprofile(request):
#   # get all todos
#   if request.method == 'GET':
#     todos = Users.objects.all()
#     serializer = UsersSerializer(todos, many=True)
#     return Response(serializer.data, safe=False)# create todo
#   elif request.method == 'POST':
#     request_data = JSONParser().parse(request)
#     serializer = UsersSerializer(data=request_data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)# purge all completed todos
#   elif request.method == 'DELETE':
#     completedToDos = Users.objects.filter(completed=True)
#     if completedToDos.count() > 0:
#       completedToDos.delete()
#     return Response({}, status=status.HTTP_204_NO_CONTENT)
  

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer
