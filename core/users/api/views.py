from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UsersSerializer, ChefSignupView, ManagerSignupView, WaiterSignupView


class ChefSignupView(generics.GenericAPIView):
    serializer_class=ChefSignupView
    def post(self, request, *args, **kwargs):
             serializer=self.get_serializer(data=request.data)
             serializer.is_valid(raise_exception=True)
             user=serializer.save()
             return Response({
                 "user":UsersSerializer(user, context=self.get_serializer_context()).data,
                 "token":Token.objects.get(user=user).key,
                 "message":"Account created successfully"
                  
             })
                          
class ManagerSignupView(generics.GenericAPIView):
    serializer_class=ManagerSignupView
    def post(self, request, *args, **kwargs):
             serializer=self.get_serializer(data=request.data)
             serializer.is_valid(raise_exception=True)
             user=serializer.save()
             return Response({
                 "user":UsersSerializer(user, context=self.get_serializer_context()).data,
                 "token":Token.objects.get(user=user).key,
                 "message":"Account created successfully"
                  
             })
             
class WaiterSignupView(generics.GenericAPIView):
    serializer_class=WaiterSignupView
    def post(self, request, *args, **kwargs):
             serializer=self.get_serializer(data=request.data)
             serializer.is_valid(raise_exception=True)
             user=serializer.save()
             return Response({
                 "user":UsersSerializer(user, context=self.get_serializer_context()).data,
                 "token":Token.objects.get(user=user).key,
                 "message":"Account created successfully"
                  
             })
             
             