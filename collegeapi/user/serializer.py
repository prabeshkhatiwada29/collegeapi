from rest_framework import serializers
from user.models import User



class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model= User
        fields = ['name', 'email', 'password', 'tc','password2']
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True}
        }
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password do not match")
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
#Login Seralizer
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password']






        

        
      
    
