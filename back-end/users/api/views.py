from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from django.views import View
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from users.models import Users
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponseServerError, JsonResponse
from django.shortcuts import get_object_or_404
import base64
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
            user_image_base64 = None
            if user.user_image:
                with open(user.user_image.path, "rb") as image_file:
                    user_image_base64 = base64.b64encode(image_file.read()).decode("utf-8")
            user_profile_data = {
                'user_id': user.pk,
                'is_chef': user.is_chef,
                'is_manager': user.is_manager,
                'is_waiter': user.is_waiter,
                'role': user.role,
                'email':user.email,
                'username':user.username,
                'fullname': user.fullname,  
                'birthdate': user.birthdate,
                'location': user.location,
                'phone': user.phone,
                'department': user.department,
                'experienceyears': user.experienceyears,
                'user_image':user_image_base64
            }
            return Response({
                'token': token.key,
                'user_profile_data':user_profile_data,
                "message": "Login successfully"
            })
        except AuthenticationFailed as e:
            
            print(f"AuthenticationFailed: {e}")
            return Response({"error": str(e)}, status=400)
        except Exception as e:
            
            print(f"Exception: {e}")
            
            return HttpResponseServerError("Internal Server Error")
             

    
class ChefOnlyView(generics.RetrieveAPIView):
    permission_classes=permissions.IsAuthenticated&IsChefUser
    serializer_class=UsersSerializer
    
    def get_object(self):
        return self.request.user
    

class WaiterOnlyView(generics.RetrieveAPIView):
    permission_classes=permissions.IsAuthenticated&IsWaiterUser
    serializer_class=UsersSerializer
    
    def get_object(self):
        return self.request.user
    
class ManagerOnlyView(generics.RetrieveAPIView):
    permission_classes=permissions.IsAuthenticated&IsManagerUser
    serializer_class=UsersSerializer
    
    def get_object(self):
        return self.request.user



class GetUserByUsernameView(View):
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        if not username:
            return JsonResponse({'error': 'Username parameter is missing'}, status=400)

        user = get_object_or_404(Users, username=username)
        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'fullname':user.fullname,
            'location':user.location,
            'role':user.role,
            'department':user.department,
            'phone':user.phone,
            'password':user.password,
            'experienceyears':user.experienceyears,
            'birthdate':user.birthdate,
            'user_image': str(user.user_image.url) if user.user_image else None,
                        
        }
        return JsonResponse(data)


class UpdateUserByUsername(generics.UpdateAPIView):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()
    lookup_field = 'username'

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class DeleteUserByUsername(generics.DestroyAPIView):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()
    lookup_field = 'username'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'User deleted successfully'})
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
             