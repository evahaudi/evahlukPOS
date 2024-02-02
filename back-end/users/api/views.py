from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed
from django.http import HttpResponseServerError
from .permissions import IsChefUser, IsWaiterUser, IsManagerUser

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
             
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        print("Request Data:", request.data)

        try:
            # Check if request.data is empty, and retrieve parameters from the URL
            if not request.data:
                username = request.query_params.get('username')
                password = request.query_params.get('password')
                data = {'username': username, 'password': password}
            else:
                data = request.data

            serializer = self.serializer_class(data=data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            print("Validated Data:", serializer.validated_data)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'is_chef': user.is_chef,
                'is_manager': user.is_manager,
                'is_waiter': user.is_waiter,
                'role':user.role,
                "message": "Login successfully"
            })
        except AuthenticationFailed as e:
            # Log the exception or print for debugging
            print(f"AuthenticationFailed: {e}")
            return Response({"error": str(e)}, status=400)
        except Exception as e:
            # Log the exception or print for debugging
            print(f"Exception: {e}")
            # Return a generic error response
            return HttpResponseServerError("Internal Server Error")
             
class LogoutView(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return  Response(status=status.HTTP_200_OK)
    
class ChefOnlyView(generics.RetrieveAPIView):
    permission_class=permissions.IsAuthenticated&IsChefUser
    serializer_class=UsersSerializer
    
    def get_object(self):
        return self.request.user
    

class WaiterOnlyView(generics.RetrieveAPIView):
    permission_class=permissions.IsAuthenticated&IsWaiterUser
    serializer_class=UsersSerializer
    
    def get_object(self):
        return self.request.user
    
class ManagerOnlyView(generics.RetrieveAPIView):
    permission_class=permissions.IsAuthenticated&IsManagerUser
    serializer_class=UsersSerializer
    
    def get_object(self):
        return self.request.user
             