# serializers.py
from rest_framework import serializers
from users.models import Users, Chef, Manager, Waiter

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'email','fullname', 'is_chef', 'is_manager', 'is_waiter', 'birthdate', 'location','experienceyears', 'phone', 'created_at', 'updated_at','department', 'role']

class ChefSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'}, write_only=True)
    user = UsersSerializer()
    class Meta:
        model = Users
        fields = ['id', 'user', 'username','fullname', 'email','password2', 'cuisine_specialty', 'experienceyears']
        extra_kwargs={
            'password':{'write_only':True}
        }

class ManagerSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'}, write_only=True)
    user = UsersSerializer()
    class Meta:
        model = Users
        fields = ['id', 'user','username', 'fullname', 'email', 'password2' 'department']
        extra_kwargs={
            'password':{'write_only':True}
        }
      
class WaiterSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'}, write_only=True)
    user = UsersSerializer()
    class Meta:
        model = Users
        fields = ['id', 'user','username', 'fullname', 'email', 'password2', 'assigned_tables']
        extra_kwargs={
            'password':{'write_only':True}
        }

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'table_number', 'capacity']

class OrderSerializer(serializers.ModelSerializer):
    waiter = WaiterSerializer()

    class Meta:
        model = Users
        fields = ['id', 'waiter', 'items', 'total_amount', 'order_date']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'price']
        
class ChefSignupView(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model=Users
        fields = ['id','username','email', 'fullname', 'birthdate', 'location','experienceyears', 'phone','department','password','password2', 'role']
        extra_kwargs={
            'password':{'write_only':True}
        }
        
    def save(self, **kwargs):
     
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        fullname=self.validated_data['fullname']
        location = self.validated_data['location']
        birthdate = self.validated_data['birthdate']
        phone = self.validated_data['phone']
        department = self.validated_data['department']
        experienceyears = self.validated_data['experienceyears']
        role= self.validated_data['role']

        if password != password2:
            raise serializers.ValidationError({"error": "Passwords do not match"})

        user = Users(
            fullname=fullname,
            username=username,
            email=email,
            location=location,
            birthdate=birthdate,
            phone=phone,
            department=department,
            experienceyears=experienceyears,
            role=role
        )
        user.set_password(password)
        user.is_chef = True
        user.save()
        Chef.objects.create(user=user)
        return user
        
class ManagerSignupView(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model=Users
        fields =  ['id','username','email', 'fullname', 'birthdate', 'location','experienceyears', 'phone','department', 'updated_by','password','password2', 'role']
        extra_kwargs={
            'password':{'write_only':True}
        }
        
    def save(self, **kwargs):
        fullname=self.validated_data['fullname']
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        location = self.validated_data['location']
        birthdate = self.validated_data['birthdate']
        phone = self.validated_data['phone']
        department = self.validated_data['department']
        experienceyears = self.validated_data['experienceyears']
        role= self.validated_data['role']

        if password != password2:
            raise serializers.ValidationError({"error": "Passwords do not match"})

        user = Users(
            fullname=fullname,
            username=username,
            email=email,
            location=location,
            birthdate=birthdate,
            phone=phone,
            department=department,
            experienceyears=experienceyears,
            role=role
        )
        user.set_password(password)
        user.is_manager = True
        user.save()
        Manager.objects.create(user=user)
        return user
        
class WaiterSignupView(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model=Users
        fields =  ['id','username','email', 'fullname', 'birthdate', 'location','experienceyears', 'phone','department', 'updated_by','password','password2', 'role']
        extra_kwargs={
            'password':{'write_only':True}
        }
        
    def save(self, **kwargs):
        fullname=self.validated_data['fullname']
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        location = self.validated_data['location']
        birthdate = self.validated_data['birthdate']
        phone = self.validated_data['phone']
        department = self.validated_data['department']
        experienceyears = self.validated_data['experienceyears']
        role= self.validated_data['role']

        if password != password2:
            raise serializers.ValidationError({"error": "Passwords do not match"})

        user = Users(
            fullname=fullname,
            username=username,
            email=email,
            location=location,
            birthdate=birthdate,
            phone=phone,
            department=department,
            experienceyears=experienceyears,
            role=role
                        
        )
        user.set_password(password)
        user.is_waiter = True
        user.save()
        Waiter.objects.create(user=user)
        return user
        
